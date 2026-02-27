from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.platform.organization import router as platform_router

# Import all phase engines here
from app.engine.phase121_engine import router as phase121_router

# Future phases will be added like this:
# from app.engine.phase122_engine import router as phase122_router


# Create FastAPI app
app = FastAPI(
    title="Aura AI Core",
    description="Autonomous Organizational Intelligence System",
    version="121.0"
)


# Enable CORS (important for future dashboard)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register phase routers
app.include_router(phase121_router)
app.include_router(platform_router)
# Future:
# app.include_router(phase122_router)


# Root endpoint
@app.get("/")
def root():
    return {
        "system": "Aura AI Core",
        "status": "ACTIVE",
        "phase": "121",
        "architecture": "ENGINE_BASED"
    }


# Health endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "core": "operational"
    }


# System status endpoint
@app.get("/system/status")
def system_status():
    return {
        "system": "Aura AI",
        "core": "running",
        "engine": "Phase 121 active",
        "deployment": "Render Cloud"
    }