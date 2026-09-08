from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, nullable=False, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False) 
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    amount = Column(Integer, nullable=False )
    status = Column(String, default="pending", nullable=False)

