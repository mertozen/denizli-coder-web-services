from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Veri modelleri
class User(BaseModel):
    id: int
    name: str
    email: str

class Product(BaseModel):
    id: int
    name: str
    price: float

# Örnek veriler
users = [
    User(id=1, name="Ali", email="ali@example.com"),
    User(id=2, name="Ayşe", email="ayse@example.com"),
]

products = [
    Product(id=1, name="Laptop", price=15000.0),
    Product(id=2, name="Telefon", price=8000.0),
]

# Endpointler
@app.get("/")
def read_root():
    return {"message": "FastAPI Başlangıç Örneği"}

@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "Kullanıcı bulunamadı"}

@app.get("/products", response_model=List[Product])
def get_products():
    return products

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Ürün bulunamadı"}
