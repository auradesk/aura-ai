from fastapi import APIRouter
from app.api.reflection_routes import router as reflection_router

router = APIRouter()
router.include_router(reflection_router, prefix="/reflection", tags=["Reflection"])

class IntelligenceRequest(BaseModel):

    tenant_id: str
    domain: str
    message: str


@router.post("/intelligence")

def intelligence(request: IntelligenceRequest):

    result = agi_engine.process(
        tenant_id=request.tenant_id,
        domain=request.domain,
        message=request.message
    )

    return {
        "status": "success",
        "tenant_id": request.tenant_id,
        "domain": request.domain,
        "intent": result["intent"],
        "response": result["response"],
        "timestamp": datetime.utcnow()
    }
