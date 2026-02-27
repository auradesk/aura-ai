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