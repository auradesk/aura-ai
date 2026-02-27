# ============================================================
# AURA AI CORE — PHASE 121 ENGINE WITH API ROUTER
# ============================================================

from datetime import datetime
import uuid

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any, List


# ============================================================
# REQUEST MODEL
# ============================================================

class AssessmentRequest(BaseModel):
    input_data: Dict[str, Any]


# ============================================================
# ENGINE
# ============================================================

class Phase121Engine:

    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    def assess(self, input_data: dict):

        assessment_id = str(uuid.uuid4())

        result = {
            "assessment_id": assessment_id,
            "timestamp": datetime.utcnow().isoformat(),
            "input": input_data,
            "cognitive_state": self._determine_state(input_data),
            "confidence": self._calculate_confidence(input_data),
            "recommendation": self._generate_recommendation(input_data)
        }

        self.history.append(result)

        return result

    def _determine_state(self, input_data):

        text = str(input_data).lower()

        if "critical" in text:
            return "CRITICAL"

        if "warning" in text:
            return "WARNING"

        return "STABLE"

    def _calculate_confidence(self, input_data):

        size = len(str(input_data))

        if size > 100:
            return 0.95

        if size > 50:
            return 0.85

        return 0.75

    def _generate_recommendation(self, input_data):

        state = self._determine_state(input_data)

        if state == "CRITICAL":
            return "Immediate intervention required"

        if state == "WARNING":
            return "Monitor closely"

        return "Continue normal operation"

    def get_history(self):

        return self.history


# ============================================================
# ENGINE INSTANCE
# ============================================================

engine = Phase121Engine()


# ============================================================
# API ROUTER
# ============================================================

router = APIRouter(
    prefix="/phase121",
    tags=["Phase121 Cognitive Engine"]
)


@router.post("/assess")
def assess(request: AssessmentRequest):

    result = engine.assess(request.input_data)

    return {
        "status": "success",
        "result": result
    }


@router.get("/history")
def history():

    return {
        "history": engine.get_history()
    }