from pydantic import BaseModel, EmailStr, ValidationError
from errors import HttpError


class CreateUser(BaseModel):

    email: EmailStr
    password: str


class CreateAd(BaseModel):
    title: str
    description: str
    user_id: int


def validate_create_user(json_data):
    try:
        user_schema = CreateUser(**json_data)
        return user_schema.dict()
    except ValidationError as er:
        raise HttpError(400, er.errors())


def validate_create_ad(json_data):
    try:
        user_schema = CreateAd(**json_data)
        return user_schema.dict()
    except ValidationError as er:
        raise HttpError(400, er.errors())
