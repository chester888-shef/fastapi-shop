from passlib.context import CryptContext
import jwt

SECRET_KEY = "arsen_loh"


pwd_context = CryptContext(schemes =["bcrypt"], deprecated = "auto")

def get_password_hash (password: str ) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password: str)-> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_token(data: dict)-> str:
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")


