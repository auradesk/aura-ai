from fastapi import APIRouter

router = APIRouter(
    prefix="/platform",
    tags=["Platform"]
)

@router.get("/status")
def platform_status():
    return {
        "platform": "Aura AI Platform Layer",
        "status": "ACTIVE"
    }