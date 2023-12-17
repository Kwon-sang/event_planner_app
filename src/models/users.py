from typing import Optional, List

from beanie import Document
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column

from .events import Event


class BaseUser(Document):
    username: str = Column(index=True, unique=True)
    password: str


class User(BaseUser):
    email: Optional[EmailStr] = None
    events: Optional[List[Event]] = None

    class Settings:
        name = "users"


class UserSignIn(BaseUser):
    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "Username",
                "password": "Password",
            }
        }
    }


class UserSignup(User):
    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "Username",
                "password": "Password",
                "email": "userEmail@google.com",
                "event": ["event1", "evnet2"]
            }
        }
    }

