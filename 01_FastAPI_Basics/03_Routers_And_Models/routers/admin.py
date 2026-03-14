from fastapi import APIRouter


router = APIRouter(prefix="/admin",tags = ["Admin"])

@router.get("/stats",status_code=200)
def admin_stats():
    return{
        "service":"User Management API",
        "status":"running"
    }