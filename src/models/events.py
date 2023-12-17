from typing import List, Optional

from pydantic import BaseModel
from beanie import Document


class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Swimming",
                "image": "http://linktoimage.com/image.jpg",
                "description": "My swimming event plan",
                "tags": ["swimming", "exercise", "hobby"],
                "location": "Osan city, kr"
            }
        }
    }

    class Settings:
        name = "events"


class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Swimming",
                "image": "http://linktoimage.com/image.jpg",
                "description": "My swimming event plan",
                "tags": ["swimming", "exercise", "hobby"],
                "location": "Osan city, kr"
            }
        }
    }
