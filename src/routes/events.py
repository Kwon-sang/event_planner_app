from typing import List, Type

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status

from src.models.events import Event, EventUpdate
from src.database.connection import Database

router = APIRouter(prefix="/events", tags=["Event"])
event_database = Database(Event)


@router.get("/")
async def retrieve_all_events() -> List[Event]:
    return await event_database.get_all()


@router.get("/{event_id}")
async def retrieve_event(event_id: PydanticObjectId) -> Event:
    if found_event := await event_database.get(event_id):
        return found_event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event ID not exist.")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_event(event_request: Event) -> dict:
    await event_database.save(event_request)
    return {"message": "Event created successfully."}


@router.put("/{event_id}")
async def update_event(event_id: PydanticObjectId, event_request: EventUpdate) -> Event:
    if updated_event := await event_database.update(event_id, event_request):
        return updated_event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event ID not exist.")


@router.delete("/{evnet_id}")
async def delete_event(event_id: PydanticObjectId):
    if await event_database.delete(event_id):
        return {"message": "Event deleted successfully."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event ID not exist.")
