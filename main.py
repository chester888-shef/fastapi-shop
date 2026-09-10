from fastapi import FastAPI, Depends, HTTPException
from database import get_db 
from models import User
from schema import UserCreate
from sqlalchemy.orm import Session
from security import get_password_hash, verify_password, create_token

app = FastAPI()

@app.post("/register")
def post_register(data: UserCreate, db:Session = Depends(get_db)):
    hashed_password = get_password_hash(data.password)
    new_user = User( username = data.username, hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    return {"messsage": "Registered"}

@app.post("/login")
def post_login(data: UserCreate, db = Depends(get_db)):
    name = db.query(User).filter(User.username == data.username).first()
    if not name:
        raise HTTPException(status_code=403,detail="Користувача під таким ім'я не знайдено")
    valid = verify_password(data.password, name.hashed_password) 
    if valid == False:
        raise HTTPException(status_code=403, detail="Пароль не вірний :)")
    data = {"sub": name.username}
    token = create_token(data)
    return {"acces_token": token, "token_type": "bearer"}