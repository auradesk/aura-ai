from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# database
from app.database import Base, engine

# routers
from app.platform_router import router as platform_router
from app.memory.memory_router import router as memory_router


# Create tables automatically (VERY IMPORTANT)
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Aura AI Core",
    description="Autonomous Organizational Intelligence Platform",
    version="124.0"
)


# Enable CORS (fixes fetch + browser issues)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routers
app.include_router(platform_router)
app.include_router(memory_router)


@app.get("/")
def root():
    return {
        "system": "Aura AI Core",
        "status": "ACTIVE",
        "phase": "124",
        "memory": "ENABLED",
        "platform": "ENABLED"
    }
@app.on_event("startup")
def recreate_db():
    from database import Base, engine
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)