from app.adapters.factory import get_adapter
from app.domains.healthcare.healthcare_engine import HealthcareEngine


class HybridBrain:

    def __init__(self):
        self.healthcare_engine = HealthcareEngine()

    def process(self, tenant_id, domain, message, memory_context=""):

        # Step 1 — Healthcare domain uses specialized engine
        if domain == "healthcare":

            healthcare_response = self.healthcare_engine.process(message)

            if healthcare_response:
                return healthcare_response

        # Step 2 — Otherwise use AI adapter (OpenAI or Local fallback)
        adapter = get_adapter()

        ai_response = adapter.generate(
            tenant_id=tenant_id,
            domain=domain,
            message=message,
            memory_context=memory_context
        )

        return ai_response
