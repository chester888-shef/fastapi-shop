from passlib.context import CryptContext
import jwt
from database import get_db
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from models import User

SECRET_KEY = "arseт"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes =["bcrypt"], deprecated = "auto")

def get_password_hash (password: str ) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password: str)-> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_token(data: dict)-> str:
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")

def decode_token(data: str)->dict:
    return jwt.decode(data, SECRET_KEY, algorithms=["HS256"])


def get_current_user(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    try:
        payload = decode_token(token)
        login = payload["sub"]
        user = db.query(User).filter(User.username == login).first()
        return user
    except Exception as e: 
        print(f"Помилка розшифровки: {e}") 
        raise HTTPException(status_code=403, detail="JWT токен не є дійсним!!!")

