from typing import List, Optional

from beanie import Document


class BaseEvent(Document):
    title: str
    description: str
    image: Optional[str] = None
    location: Optional[str] = None
    tags: Optional[List[str]] = None


class Event(BaseEvent):
    owner: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Go to Swimming",
                "image": "http://linktoimage.com/image.jpg",
                "description": "My swimming event plan",
                "tags": ["swimming", "exercise", "hobby"],
                "location": "Osan city, kr"
            }
        }
    }

    class Settings:
        name = "events"


class EventUpdate(BaseEvent):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
