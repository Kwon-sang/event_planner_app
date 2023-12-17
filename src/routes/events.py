from fastapi import APIRouter


router = APIRouter(prefix="/events", tags=["Event"])

events = []


@router.get("/")
async def retrieve_all_events():
    # Todo
    pass

@router.get("/{event_id}")
async def retrieve_event():
    # Todo
    pass


@router.post("/")
async def create_event():
    # Todo
    pass


@router.put("/{event_id}")
async def update_event():
    # Todo
    pass


@router.delete("/{evnet_id}")
async def delete_event():
    # Todo
    pass