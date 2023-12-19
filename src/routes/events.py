from typing import List, Annotated

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status, Depends

from src.models.events import Event, EventUpdate
from src.database.connection import Database
from src.auth.authentication import authenticate

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
async def create_event(user: Annotated[str, Depends(authenticate)],
                       event: Event) -> dict:
    event.owner = user
    await event_database.save(event)
    return {"message": "Event created successfully."}


@router.put("/{event_id}")
async def update_event(user: Annotated[str, Depends(authenticate)],
                       event_id: PydanticObjectId, event: EventUpdate) -> Event:
    # Validate resource owner
    db_event = await event_database.get(event_id)
    if db_event.owner != user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation is not allowed.")
    # Update resource
    if updated_event := await event_database.update(event_id, event):
        return updated_event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event ID not exist.")


@router.delete("/{evnet_id}")
async def delete_event(user: Annotated[str, Depends(authenticate)],
                       event_id: PydanticObjectId):
    # Validate resource owner
    db_event = await event_database.get(event_id)
    if db_event.owner != user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation is not allowed.")
    if await event_database.delete(event_id):
        return {"message": "Event deleted successfully."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event ID not exist.")
