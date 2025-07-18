from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

fake_users_db: Dict[int, dict] = {
    1: {"name": "Ali", "email": "ali@example.com", "password": 1234},
    2: {"name": "Mert", "email": "mert@example.com", "password": 232323},
    3: {"name": "Veli", "email": "veli@example.com", "password": 343434},
}

class User(BaseModel):
    name: str
    email: str
    password: str

class UserPatch(BaseModel):
    name: str | None = None
    email: str | None = None

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")
    fake_users_db[user_id] = user.model_dump()
    return fake_users_db[user_id]

@app.post("/users1/{user_id}")
def patch_user(user_id: int, user: UserPatch):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")
    stored_user = fake_users_db[user_id]
    update_data = user.model_dump(exclude_unset=True)
    stored_user.update(update_data)
    fake_users_db[user_id] = stored_user
    return fake_users_db[user_id]

@app.get("/users")
def get_users():
    return fake_users_db