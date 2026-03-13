from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr

app = FastAPI(title="FastAPI Fetch & Update by User ID")

users = {
    1:{
        "name": "user1",
        "email": "user1@example.com",
        "age": 27
    },
    2:{
        "name": "user2",
        "email": "user2@example.com",
        "age":35
    }
}

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

#fetch user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404,detail="User not found")
    return users[user_id]


#update user by ID
@app.put("/users/{user_id}")
def update_user(user_id: int,user:User):
    if user_id not in users:
        raise HTTPException(status_code=404,detail="User not found")

    users[user_id] = user
    return {"message": "User updated successfully","user":user}

