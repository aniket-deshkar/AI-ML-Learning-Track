#refactor API into multiple routers
from fastapi import FastAPI
from routers import users,health,admin


app = FastAPI(title="FastAPI Router and Request Model")


@app.get("/")
def root():
    return "FastAPI Router"


app.include_router(users.router)
app.include_router(health.router)
app.include_router(admin.router)