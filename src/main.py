from fastapi import FastAPI

from src.database.connection import Database
from src.routes import users, events


app = FastAPI()
app.include_router(router=users.router)
app.include_router(router=events.router)


@app.on_event("startup")
async def init_db():
    await Database.init_db()
