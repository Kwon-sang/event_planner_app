from typing import List, Optional

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


class EventUpdate(Event):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
