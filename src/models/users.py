from typing import Optional, List

from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr

from .events import Event


class BaseUser(Document):
    username: Indexed(str, unique=True)
    password: str


class User(BaseUser):
    email: Optional[EmailStr] = None
    events: Optional[List[Event]] = None

    class Settings:
        name = "users"


class UserSignup(BaseUser):
    email: Optional[EmailStr] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "username",
                "password": "password",
                "email": "userEmail@google.com"
            }
        }
    }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
