from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from sqlalchemy import event

from src.models.events import Event
from src.database.connection import Database

router = APIRouter(prefix="/events", tags=["Event"])
event_database = Database(Event)


@router.get("/", response_model=List[Event], status_code=status.HTTP_200_OK)
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events


@router.get("/{event_id}", response_model=Event)
async def retrieve_event(event_id: PydanticObjectId) -> Event:
    event = await event_database.get(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Event with supplied ID does not exist.")
    return event


@router.post("/")
async def create_event(event_request: Event) -> dict:
    await event_database.save(event_request)
    return {"message": "Event created successfully."}


@router.put("/{event_id}", response_model=Event)
async def update_event(event_id: PydanticObjectId, event_request: Event) -> Event:
    updated_event = await event_database.update(event_id, event_request)
    if not updated_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Event with supplied ID does not exist.")
    return updated_event


@router.delete("/{evnet_id}")
async def delete_event(event_id: PydanticObjectId):
    event = await event_database.delete(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Event with supplied ID does not exist.")
    return {"message": "Event deleted successfully."}