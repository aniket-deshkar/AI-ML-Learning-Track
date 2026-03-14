from fastapi import FastAPI,Query
from pydantic import BaseModel,EmailStr

app = FastAPI()

users = {}
user_id_counter = 1

#Request Model
class User_create(BaseModel):
    username:str
    email:EmailStr
    age:int


#Internal Model
class User_internal(BaseModel):
    id:int
    username:str
    email:EmailStr
    age:int
    is_admin:bool = False

#Response Model
class User_response(BaseModel):
    id:int
    username:str
    email:EmailStr
    age:int


#API
@app.post("/users",response_model=User_response)
def create_user(user: User_create):
    global user_id_counter

    internal_user = User_internal(
        id=user_id_counter,
        username=user.username,
        email=user.email,
        age=user.age
    )

    users[user_id_counter] = internal_user
    user_id_counter += 1
    return internal_user


#pagination
@app.get("/users",response_model=list[User_response])
def get_users(
    page:int = Query(1,ge=1),
    size:int = Query(5,ge=1,le=50)
):
    user_list = list(users.values())

    start = (page-1)* size
    end = start + size

    return user_list[start:end]