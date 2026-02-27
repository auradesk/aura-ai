# ============================================================
# AURA AI CORE V2
# Professional Live Intelligence Engine
# ============================================================
from database import SessionLocal, init_db, SystemMetric, IntelligenceScore

init_db()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random
import asyncio
from typing import Dict
from database import SessionLocal, SystemMetric
from app.engine.phase121_engine import Phase121Engine
from memory_engine import init_memory, store_memory, get_recent_memories
# Phase121 Engine
try:
    from app.engine.phase121_engine import router as phase121_router
    app.include_router(phase121_router)
    print("Phase121 Engine Loaded")
except Exception as e:
    print("Phase121 Engine Failed:", e)
# ============================================================
# APP INITIALIZATION
# ============================================================

from fastapi import FastAPI

app = FastAPI(
    title="Aura AI Core",
    version="122.0"
)

# import phase121 router
from app.engine.phase121_engine import router as phase121_router

app.include_router(phase121_router)


@app.get("/")
def root():
    return {"system": "Aura AI Core", "status": "ACTIVE"}

init_memory()
phase121_engine = Phase121Engine()
# Enable CORS (required for dashboard connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# GLOBAL SYSTEM STATE
# ============================================================

aura_state: Dict = {
    "system_status": "ACTIVE",
    "core_version": "2.0.0",
    "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "last_update": None,

    "domains": {
        "healthcare": 0,
        "business": 0,
        "education": 0
    },

    "performance": {
        "cpu_load": 0,
        "memory_usage": 0,
        "response_time_ms": 0
    }
}

# ============================================================
# LIVE SCORE GENERATOR
# ============================================================

def generate_live_scores():
    """Simulates real AI intelligence scoring"""

    aura_state["domains"]["healthcare"] = random.randint(85, 98)
    aura_state["domains"]["business"] = random.randint(80, 97)
    aura_state["domains"]["education"] = random.randint(82, 99)

    aura_state["performance"]["cpu_load"] = random.randint(10, 65)
    aura_state["performance"]["memory_usage"] = random.randint(20, 70)
    aura_state["performance"]["response_time_ms"] = random.randint(45, 180)

    aura_state["last_update"] = datetime.now().strftime("%H:%M:%S")

# ============================================================
# BACKGROUND LIVE UPDATE LOOP
# ============================================================

async def live_update_loop():
    """Continuously updates Aura intelligence"""
    while True:
        generate_live_scores()
        await asyncio.sleep(5)

# ============================================================
# STARTUP EVENT
# ============================================================

@app.on_event("startup")
async def startup_event():
    print("Aura Core starting...")
    asyncio.create_task(live_update_loop())
    print("Aura Core ACTIVE")

# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
async def root():
    return {
        "system": "Aura AI Core",
        "status": aura_state["system_status"],
        "version": aura_state["core_version"]
    }

# ============================================================
# HEALTH CHECK ENDPOINT
# ============================================================

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "system_status": aura_state["system_status"],
        "last_update": aura_state["last_update"]
    }

# ============================================================
# MAIN CONTROL CENTER ENDPOINT
# ============================================================

@app.post("/phase121/assess")
async def phase121_assess():
    """Main endpoint used by Professional Control Center"""

    generate_live_scores()

    return {
        "status": aura_state["system_status"],
        "core_version": aura_state["core_version"],
        "domains": aura_state["domains"],
        "performance": aura_state["performance"],
        "last_update": aura_state["last_update"]
    }

# ============================================================
# FULL SYSTEM STATUS ENDPOINT
# ============================================================

@app.get("/system/status")
async def system_status():
    return aura_state

# ============================================================
# DOMAIN SPECIFIC ENDPOINTS
# ============================================================

@app.get("/domain/healthcare")
async def healthcare_status():
    return {
        "domain": "healthcare",
        "score": aura_state["domains"]["healthcare"],
        "last_update": aura_state["last_update"]
    }

@app.get("/domain/business")
async def business_status():
    return {
        "domain": "business",
        "score": aura_state["domains"]["business"],
        "last_update": aura_state["last_update"]
    }

@app.get("/domain/education")
async def education_status():
    return {
        "domain": "education",
        "score": aura_state["domains"]["education"],
        "last_update": aura_state["last_update"]
    }

# ============================================================
# SYSTEM CONTROL ENDPOINTS
# ============================================================

@app.post("/system/activate")
async def activate_system():
    aura_state["system_status"] = "ACTIVE"
    return {"status": "Aura Core ACTIVATED"}

@app.post("/system/standby")
async def standby_system():
    aura_state["system_status"] = "STANDBY"
    return {"status": "Aura Core in STANDBY"}

@app.get("/metrics/history")
def history():

    db = SessionLocal()

    data = db.query(SystemMetric)\
        .order_by(SystemMetric.timestamp.desc())\
        .limit(100)\
        .all()

    db.close()

    return data
from fastapi import Request

@app.post("/chat")
async def chat(request: Request):

    data = await request.json()
    user_input = data.get("message", "")

    aura_response = f"Aura received: {user_input}"

    store_memory(user_input, aura_response)

    return {
        "response": aura_response
    }
@app.get("/memory")
def memory():

    memories = get_recent_memories()

    return {
        "memories": memories
    }
app.include_router(phase41_router)
@app.get("/health")
def health():
    return {"status": "healthy", "aura": "operational"}

# ============================================
# PHASE 122 — ORGANIZATION PLATFORM LAYER
# Aura becomes multi-tenant ecosystem
# ============================================

from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime
import uuid

# ============================================
# Organization Model
# ============================================

class OrganizationCreate(BaseModel):
    name: str
    domain: str  # healthcare, business, education
    admin_email: str


class Organization(BaseModel):
    org_id: str
    name: str
    domain: str
    admin_email: str
    created_at: str
    status: str


# ============================================
# Organization Registry
# ============================================

ORGANIZATIONS: Dict[str, Organization] = {}


# ============================================
# Register Organization
# ============================================

@app.post("/platform/organization/register")
def register_organization(org: OrganizationCreate):

    org_id = f"ORG-{uuid.uuid4().hex[:8].upper()}"

    new_org = Organization(
        org_id=org_id,
        name=org.name,
        domain=org.domain,
        admin_email=org.admin_email,
        created_at=datetime.utcnow().isoformat(),
        status="ACTIVE"
    )

    ORGANIZATIONS[org_id] = new_org

    return {
        "status": "SUCCESS",
        "message": "Organization registered on Aura platform",
        "organization": new_org
    }


# ============================================
# Get Organization
# ============================================

@app.get("/platform/organization/{org_id}")
def get_organization(org_id: str):

    org = ORGANIZATIONS.get(org_id)

    if not org:
        return {"error": "Organization not found"}

    return org


# ============================================
# List Organizations
# ============================================

@app.get("/platform/organizations")
def list_organizations():

    return {
        "total": len(ORGANIZATIONS),
        "organizations": ORGANIZATIONS
    }


# ============================================
# Platform Status
# ============================================

@app.get("/platform/status")
def platform_status():

    return {
        "platform": "Aura AI Ecosystem",
        "status": "ACTIVE",
        "organizations": len(ORGANIZATIONS),
        "phase": "122",
        "level": "PLATFORM"
    }