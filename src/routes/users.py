from fastapi import APIRouter, HTTPException, status

from models.users import UserSignup


router = APIRouter(prefix="/users", tags=["User"])

users = {}


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user_request: UserSignup) -> dict:
    if user_request.username in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with supplied username exists")
    users.update({user_request.username: user_request})
    return {"message": "User successfully registered!"}

