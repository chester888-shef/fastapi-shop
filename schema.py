from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str
    password: str

class ProductCreate(BaseModel):
    name: str
    price: int = Field(gt=0, description="Ціна повинна бути більше 0!")

class OrderCreate(BaseModel):
    amount: int = Field(gt=0, description="Кількість повинна бути більше 0!")
    product_id: int 




