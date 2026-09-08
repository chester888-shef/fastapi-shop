from fastapi import FastAPI, Depends
from database import get_db 
from models import User
from schema import UserCreate
from sqlalchemy.orm import Session
from security import get_password_hash

app = FastAPI()

@app.post("/register")
def post_register(data: UserCreate, db:Session = Depends(get_db)):
    hashed_password = get_password_hash(data.password)
    new_user = User( username = data.username, hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    return {"messsage": "Registered"}
