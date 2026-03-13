
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token, create_refresh_token, authenticate_user

from dependencies import get_current_user, require_admin

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": create_access_token(user["username"], user["role"]),
        "refresh_token": create_refresh_token(user["username"]),
        "token_type": "bearer"
    }


@app.post("/refresh")
def refresh_token(token: str):
    from jose import jwt
    from auth import SECRET_KEY, ALGORITHM

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        return {"access_token": create_access_token(username, "user")}
    except:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


@app.get("/user")
def user_route(user=Depends(get_current_user)):
    return {"message": "User access granted", "user": user}


@app.get("/admin")
def admin_route(admin=Depends(require_admin)):
    return {"message": "Admin access granted", "admin": admin}
