from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashPassword:
    def create_hash(self, password: str):
        return pwd_context.hash(secret=password)

    def verify_hash(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(secret=plain_password, hash=hashed_password)
