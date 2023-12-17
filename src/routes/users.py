from fastapi import APIRouter, HTTPException, status

from ..database.connection import Database
from ..models.users import User, UserSignup, UserSignIn

router = APIRouter(prefix="/users", tags=["User"])
user_database = Database(model=User)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user_request: UserSignup) -> dict:
    if await User.get(document_id=user_request.id):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exist.")
    await user_database.save(user_request)
    return {"message": "User created successfully."}


@router.post("/signin")
async def signin(user_request: UserSignIn):
    user_exist = await User.find_one(User.username == user_request.username)
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist.")
    if user_exist.password != user_request.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid user.")
    return {"message": "Login successfully."}

