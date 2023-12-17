from pydantic import BaseModel
from typing import List


class Event(BaseModel):
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