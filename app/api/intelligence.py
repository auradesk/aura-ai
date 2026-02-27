from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal  # your database session
from app.engine.agi_engine import AGIEngine

router = APIRouter()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/process")
def process_intelligence(
    tenant_id: str,
    domain: str,
    input_text: str,
    db: Session = Depends(get_db)
):
    """
    Process input through AGIEngine:
    - recall existing memory
    - reinforce confidence/importance
    - create new memory if needed
    - return response
    """

    agi = AGIEngine(db)

    response = agi.process_input(
        tenant_id=tenant_id,
        domain=domain,
        input_text=input_text
    )

    return {
        "response": response,
        "status": "learned"
    }
from app.engine.memory_consolidation_engine import MemoryConsolidationEngine

consolidation_engine = MemoryConsolidationEngine()


@router.post("/consolidate")
def consolidate_memory(request: dict):

    result = consolidation_engine.consolidate_memories(
        tenant_id=request["tenant_id"],
        domain=request["domain"]
    )

    return {
        "status": "success",
        "consolidation": result
    }
from fastapi import APIRouter
from AURA.AURA_CORE_V2.main import agi_engine

router = APIRouter()


@router.post("/reflect")
def reflect(data: dict):

    goal = data.get("goal")
    plan = data.get("plan", [])
    results = data.get("results", [])

    reflection = agi_engine.reflect(goal, plan, results)

    return {
        "status": "reflection_complete",
        "reflection": reflection
    }