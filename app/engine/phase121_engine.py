from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

router = APIRouter()

# ==========================
# REQUEST MODEL
# ==========================

class Phase121Input(BaseModel):
    source: str
    domain: Optional[str] = "general"
    message: str


# ==========================
# SYSTEM STATUS (Simple)
# ==========================

SYSTEM_STATUS = "ACTIVE"


# ==========================
# ASSESS ENDPOINT
# ==========================

@router.post("/phase121/assess")
async def phase121_assess(payload: Phase121Input):

    if SYSTEM_STATUS != "ACTIVE":
        return {
            "status": "SYSTEM_NOT_ACTIVE",
            "message": "Aura is currently not active",
            "phase": 41
        }

    response_text = (
        f"[Phase 41 Cognitive Layer] "
        f"Source: {payload.source} | "
        f"Domain: {payload.domain} | "
        f"Message: {payload.message}"
    )

    return {
        "aura_response": response_text,
        "system_status": SYSTEM_STATUS,
        "phase": 41,
        "timestamp": datetime.utcnow().isoformat()
    }