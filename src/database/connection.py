from typing import Any, Optional, List

from pydantic import BaseConfig
from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.events import Event
from ..models.users import User


class Settings(BaseConfig):
    MONGO_DB_URL = "mongodb://localhost:27017/planner"
    SECRET_KEY: Optional[str] = "HI5HL3SFSD$S"

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.MONGO_DB_URL)
        await init_beanie(database=client.get_default_database(), document_models=[Event, User])


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, body: Any):
        await body.create()

    async def get(self, _id: PydanticObjectId) -> Optional[Any]:
        doc = await self.model.get(document_id=_id)
        return doc if doc else None

    async def get_all(self) -> List[Any]:
        return await self.model.find_all().to_list()

    async def update(self, _id: PydanticObjectId, body) -> Any:
        body_dict = body.model_dump(exclude_none=True)
        update_query = {
            "$set": {key: value for key, value in body_dict.items() if value}
        }
        if doc := await self.get(_id):
            await doc.update(update_query)
            return doc
        return None

    async def delete(self, _id: PydanticObjectId) -> bool:
        if doc := await self.get(_id):
            await doc.delete()
            return True
        return False
