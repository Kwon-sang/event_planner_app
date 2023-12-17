from typing import Any

from pydantic import BaseConfig, BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document, PydanticObjectId

from src.models.events import Event


class Settings(BaseConfig):
    MONGO_URL = "mongodb://localhost:27017/planner"

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.MONGO_URL)
        await init_beanie(database=client.get_default_database(), document_models=[Event])


class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document: Document):
        await document.create()
        return

    async def get(self, model_id: PydanticObjectId) -> Any:
        document = await self.model.get(model_id)
        if document:
            return document
        return False

    async def get_all(self):
        documents = await self.model.find_all().to_list()
        return documents


    async def update(self, model_id: PydanticObjectId, body: BaseModel) -> Any:
        document_id = model_id
        descript_body = body.model_dump(exclude_none=True)
        update_query = {
            "$set": {field: value for field, value in descript_body.items()}
        }
        document = await self.get(document_id)
        if not document:
            return False
        await document.update(update_query)
        return document

    async def delete(self, model_id: PydanticObjectId) -> bool:
        doc = await self.get(model_id)
        if not doc:
            return False
        await doc.delete()
        return True
