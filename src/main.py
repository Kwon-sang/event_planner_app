from fastapi import FastAPI

from routes import users, events

app = FastAPI()
app.include_router(router=users.router)
app.include_router(router=events.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
