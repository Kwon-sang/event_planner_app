from typing import Optional, List

from pydantic import BaseModel, EmailStr

from .events import Event


class BaseUser(BaseModel):
    username: str
    password: str

class User(BaseUser):
    pass

class UserSignup(BaseUser):
    email: Optional[str] = None
    events: Optional[List[Event]] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "UserEmail@gmail.com",
                "username": "User Name",
                "password": "User Password",
                "events": []
            }
        }
    }


class UserSignIn(BaseModel):
    username: str
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "User Name",
                "password": "User Password"
            }
        }
    }