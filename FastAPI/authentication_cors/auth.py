from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

#Generated using openssl rand -hex 32
SECRET_KEY = "b02d0700387d366fb260d3360091befe356e346b85ad1aef136ba78dfdc293bf"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {
    "user1": {
        "username": "user",
        "hashed_password": "userpass",
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "hashed_password": "adminpass",
        "role": "admin"
    }
}

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

def create_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + expires_delta
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_access_token(username: str, role: str):
    return create_token(
        {"sub": username, "role": role},
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

def create_refresh_token(username: str):
    return create_token(
        {"sub": username},
        timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    )