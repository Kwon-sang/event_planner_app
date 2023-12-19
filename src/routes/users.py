from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from ..database.connection import Database
from ..models.users import User, UserSignup, TokenResponse
from ..auth.hash_password import HashPassword
from ..auth.jwt_handler import create_access_token

router = APIRouter(prefix="/users", tags=["User"])
user_database = Database(model=User)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserSignup) -> dict:
    # Validate whether the user already registered.
    if await User.find_one(User.username == user.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exist.")
    # If not, Hashing the password.
    user.password = HashPassword.create_hash(user.password)
    # And save user to database.
    await user_database.save(User(**user.model_dump()))
    return {"message": "User created successfully."}


@router.post("/signin")
async def signin(user: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response) -> TokenResponse:
    db_user = await User.find_one(User.username == user.username)
    # Validate whether the user is in database through username.
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist.")
    # Validate hashed password and Issue token
    if HashPassword.verify_hash(user.password, db_user.password):
        access_token = create_access_token(db_user.username)
        token_type = "Bearer"
        response.headers["WWW-Authenticate"] = f"{token_type} {access_token}"
        return TokenResponse(access_token=access_token, token_type=token_type)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access.")

