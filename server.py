from flask import Flask, request, jsonify
from flask.views import MethodView
from db import User, Ad, Session

from errors import HttpError
from schema import validate_create_user, validate_create_ad

app = Flask('server')


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    http_response = jsonify({'status': 'error', 'description': error.message})
    http_response.status_code = error.status_code
    return http_response


def get_user(user_id: int, session: Session):
    user = session.query(User).get(user_id)
    if user is None:
        raise HttpError(404, 'user not found')
    return user


def get_ad(ad_id: int, session: Session):
    ad = session.query(Ad).get(ad_id)
    if ad is None:
        raise HttpError(404, 'ad not found')
    return ad


class UserView(MethodView):

    def get(self, user_id):
        with Session() as session:
            user = get_user(user_id, session)
            return jsonify(
                {
                    'id': user.id,
                    'email': user.email,
                }
            )

    def post(self):
        json_data = validate_create_user(request.json)
        with Session() as session:
            new_user = User(**json_data)
            session.add(new_user)
            session.commit()
            return jsonify(
                {
                    'id': new_user.id,
                }
            )

    def patch(self, user_id):
        json_data = request.json
        with Session() as session:
            user = get_user(user_id, session)
            for field, value in json_data.items():
                setattr(user, field, value)
            session.add(user)
            session.commit()

    def delete(self, user_id):
        with Session() as session:
            user = get_user(user_id, session)
            session.delete(user)
            session.commit()


class AdView(MethodView):

    def get(self, ad_id):
        with Session() as session:
            ad = get_user(ad_id, session)
            return jsonify(
                {
                    'id': ad.id,
                    'title': ad.title,
                    'description': ad.description,
                }
            )

    def post(self):
        json_data = validate_create_ad(request.json)
        with Session() as session:
            new_ad = Ad(**json_data)
            session.add(new_ad)
            session.commit()
            return jsonify(
                {
                    'id': new_ad.id,
                }
            )

    def patch(self, ad_id):
        json_data = request.json
        with Session() as session:
            ad = get_ad(ad_id, session)
            for field, value in json_data.items():
                setattr(ad, field, value)
            session.add(ad)
            session.commit()

    def delete(self, ad_id):
        with Session() as session:
            ad = get_ad(ad_id, session)
            session.delete(ad)
            session.commit()


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_with_id'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/users', view_func=UserView.as_view('create_user'), methods=['POST'])

app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ads_with_id'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/ads', view_func=AdView.as_view('create_ad'), methods=['POST'])


app.run(port=5001)
