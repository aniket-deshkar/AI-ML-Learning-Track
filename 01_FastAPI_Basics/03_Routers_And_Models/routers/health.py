from fastapi import APIRouter
from datetime import datetime

router = APIRouter(tags=["Health"])

@router.get("/health")
def health():
    return {
        "status": "UP",
        "timestamp": datetime.now().isoformat()
    }