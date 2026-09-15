from fastapi import FastAPI, Depends, HTTPException
from database import get_db 
from models import User, Product, Order
from schema import UserCreate, OrderCreate, ProductCreate
from sqlalchemy.orm import Session
from security import get_password_hash, verify_password, create_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

@app.post("/register")
def post_register(data: UserCreate, db:Session = Depends(get_db)):
    hashed_password = get_password_hash(data.password)
    new_user = User( username = data.username, hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    return {"messsage": "Registered"}


@app.post("/login")
def post_login(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):
    name = db.query(User).filter(User.username == form_data.username).first()
    if not name:
        raise HTTPException(status_code=403, detail="Користувача під таким ім'я не знайдено")
    valid = verify_password(form_data.password, name.hashed_password) 
    if valid == False:
        raise HTTPException(status_code=403, detail="Пароль не вірний :)")
    token_data = {"sub": name.username}
    token = create_token(token_data)
    return {"access_token": token, "token_type": "bearer"}



@app.post("/products")
def post_products(data: ProductCreate, db = Depends(get_db)):
    product =  Product(name = data.name, price = data.price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@app.get("/products")
def get_products(db = Depends(get_db)):
    all_product = db.query(Product).all()
    return all_product

@app.post("/orders")
def post_order( data: OrderCreate, db = Depends(get_db), user = Depends(get_current_user)):
    new_order = Order(amount = data.amount, product_id = data.product_id, user_id = user.id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@app.get("/see_orders")
def get_orders(db = Depends(get_db), user = Depends(get_current_user) ):
    database_info = db.query(Order).filter(Order.user_id == user.id).all()
    return database_info   