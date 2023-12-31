import time
from datetime import datetime
from typing import Optional

from fastapi import HTTPException, status
from jose import jwt, JWTError

SECRET_KEY: Optional[str] = "HI5HL3SFSD$S"


def create_access_token(user: str):
    payload = {
        "user": user,
        "expires": time.time() + 3600
    }
    token = jwt.encode(algorithm="HS256", claims=payload, key=SECRET_KEY)
    return token


def verify_access_token(token: str) -> dict:
    try:
        data = jwt.decode(algorithms="HS256", token=token, key=SECRET_KEY)
        expire = data.get("expires")
        if expire is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No access token.")
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token expired.")
        return data
    except JWTError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token.")
