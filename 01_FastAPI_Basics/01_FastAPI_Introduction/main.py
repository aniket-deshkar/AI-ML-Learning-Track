from typing import Any, Optional
from pydantic import BaseModel, EmailStr, Field
from fastapi import FastAPI, HTTPException, status
import datetime

#instantiate fastapi library
app = FastAPI(title="FastAPI Basics Mini Project")

#in_memory db
users_db = {1:
            { "username": "defaultUser",
              "email": "defaultuser@example.com",
              "age": 18}
            }


class AddUser(BaseModel):
    username: str
    email: EmailStr | None=Field(default = None)
    age: int = Field(gt=18, lt=100, description="Age must be between 18 and 100")

class UpdateUser(BaseModel):
    id :int
    username: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int] = Field(gt=18, lt=100, description="Age must be between 18 and 100")

@app.get("/")
def root():
    return {"message": "FastAPI Basics Mini Project"}

@app.get("/health")
def health_root():
    return {"status": "ok", "Timestamp": datetime.datetime.now().isoformat(),"Server staus":status.HTTP_200_OK}

@app.post("/create_user")
async def create_item(user_id : int, user: AddUser) -> dict[str, Any]:
    users_db[user_id] = user
    return {"Added": user_id, "Server Status": status.HTTP_201_CREATED}


@app.get("/get_user/{user_id}")
async def get_item(user_id: int):
        if user_id not in users_db:
            return {"User id": users_db[user_id],"Server Status": status.HTTP_200_OK }
        else:
            raise HTTPException(status_code=404, detail="User not found")

@app.get("/get_all_users/")
async def get_item(limit: int = 10):
    if users_db.items() is None:
        raise HTTPException(status_code=404, detail="No users in database")
    else:
        return {"Users in list": users_db[:limit]}

@app.put("/update_user/{user_id}")
def update_item(user_id: int, user: UpdateUser):
    users_db[user_id] = user
    return {"Updated": user, "server status": status.HTTP_302_FOUND}

@app.delete("/delete_user/{user_id}")
def delete_item(user_id: int):
    del users_db[user_id]
    return {"Deleted": user_id, "HTTP Status": status.HTTP_202_ACCEPTED}
