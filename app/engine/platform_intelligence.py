# ============================================================
# AURA AI — Phase 123 Intelligence Layer
# Organization Intelligence Engine
# ============================================================

from datetime import datetime
from typing import Dict
import uuid


class OrganizationIntelligence:

    def __init__(self, organization_id: str):
        self.intelligence_id = str(uuid.uuid4())
        self.organization_id = organization_id

        self.status = "ACTIVE"

        self.capabilities = {
            "decision_making": True,
            "learning": True,
            "adaptation": True,
            "optimization": True
        }

        self.created_at = datetime.utcnow()

    def to_dict(self):

        return {
            "intelligence_id": self.intelligence_id,
            "organization_id": self.organization_id,
            "status": self.status,
            "capabilities": self.capabilities,
            "created_at": self.created_at.isoformat()
        }


class PlatformIntelligenceEngine:

    def __init__(self):

        self.intelligence_registry: Dict[str, OrganizationIntelligence] = {}

    # ========================================================
    # Activate Intelligence
    # ========================================================

    def activate_intelligence(self, organization_id: str):

        if organization_id in self.intelligence_registry:

            return self.intelligence_registry[organization_id].to_dict()

        intelligence = OrganizationIntelligence(organization_id)

        self.intelligence_registry[organization_id] = intelligence

        return intelligence.to_dict()

    # ========================================================
    # Get intelligence for organization
    # ========================================================

    def get_intelligence(self, organization_id: str):

        if organization_id not in self.intelligence_registry:

            return {
                "status": "NOT_FOUND",
                "organization_id": organization_id
            }

        return self.intelligence_registry[organization_id].to_dict()

    # ========================================================
    # Get all intelligence systems
    # ========================================================

    def get_all_intelligence(self):

        return {

            "total": len(self.intelligence_registry),

            "systems": [

                intelligence.to_dict()

                for intelligence in self.intelligence_registry.values()
            ]
        }


# Global instance
platform_intelligence = PlatformIntelligenceEngine()