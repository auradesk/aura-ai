from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

router = APIRouter()

# ==========================
# PHASE 121 INPUT MODEL
# ==========================

class Phase121Input(BaseModel):
    source: str
    domain: Optional[str] = "general"
    message: str


# ==========================
# SIMPLE SYSTEM STATUS CHECK
# (Safe fallback if your system module changes)
# ==========================

SYSTEM_STATUS = "ACTIVE"

def get_system_status():
    return SYSTEM_STATUS


# ==========================
# PHASE 121 ASSESS ENDPOINT
# (Upgraded to Phase 41 Logic)
# ==========================

@router.post("/phase121/assess")
def phase121_assess(data: Phase121Input):

    system_status = get_system_status()

    # Block if system not active
    if system_status != "ACTIVE":
        return {
            "status": "SYSTEM_NOT_ACTIVE",
            "message": "Aura is currently not active",
            "phase": 41
        }

    # Simulated reasoning layer
    processed_response = f"[Phase 41 Cognitive Layer] Source: {data.source} | Domain: {data.domain} | Message: {data.message}"

    return {
        "aura_response": processed_response,
        "system_status": system_status,
        "phase": 41,
        "timestamp": datetime.utcnow().isoformat()
    }