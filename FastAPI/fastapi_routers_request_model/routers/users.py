from fastapi import FastAPI,HTTPException,status,APIRouter
from pydantic import BaseModel
from datetime import datetime

# In-memory storage
users = {}
user_id_counter = 1


router = APIRouter(prefix="/users",tags=["Users"])

# User model
class User(BaseModel):
    name: str
    email: str
    age: int

# a. Create a user
@router.post("/users", status_code = status.HTTP_201_CREATED)
def create_user(user: User):
    global user_id_counter
    users[user_id_counter] = user
    user_id_counter += 1
    return {"id": user_id_counter - 1, "user": user}

# b. fetch all users
@router.get("/users")
def get_all_users():
    return users

# c. fetch user by id
@router.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return users[user_id]

# d. update user details
@router.put("/users/{user_id}")
def update_user(user_id: int,user: User):
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    users[user_id] = user
    return {"message": "User Updated","user":user}

# e. Delete a user
@router.delete("/user/{user_id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    del users[user_id]
    return {"message": "User deleted"}