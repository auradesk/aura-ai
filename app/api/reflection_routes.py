# reflection_routes.py
from fastapi import APIRouter
from app.engine.memory_reflection_engine import MemoryReflectionEngine

router = APIRouter()
reflection_engine = MemoryReflectionEngine()

@router.post("/memory/store")
def store_memory(context: str, result: str):
    reflection_engine.store_memory(context, result)
    return {"status": "success", "message": "Memory stored"}

@router.get("/memory/retrieve")
def retrieve_memories(limit: int = 5):
    memories = reflection_engine.retrieve_memories(limit)
    return {"status": "success", "memories": memories}

@router.get("/memory/reflect")
def reflect_memories():
    reflections = reflection_engine.reflect()
    return {"status": "success", "reflections": reflections}