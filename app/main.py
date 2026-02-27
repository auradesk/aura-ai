from fastapi import FastAPI

# Core system
from app.database import Base, engine

# Platform router
from app.platform_router import router as platform_router

# Memory router
from app.memory.memory_router import router as memory_router


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI app
app = FastAPI(
    title="Aura AI Core",
    version="2.0",
    description="Aura AI Autonomous Intelligence Platform"
)


# Root endpoint
@app.get("/")
def root():
    return {
        "system": "Aura AI Core",
        "status": "RUNNING"
    }


# Register routers
app.include_router(platform_router)
app.include_router(memory_router)