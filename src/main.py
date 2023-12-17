from fastapi import FastAPI

from src.database.connection import Settings
from src.routes import users, events

app = FastAPI()
app.include_router(router=users.router)
app.include_router(router=events.router)


@app.on_event("startup")
async def init_db():
    settings = Settings()
    await settings.initialize_database()
