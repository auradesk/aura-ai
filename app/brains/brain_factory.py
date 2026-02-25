from app.brains.healthcare_brain import HealthcareBrain
from app.brains.business_brain import BusinessBrain


class BrainFactory:

    @staticmethod
    def create_brain(tenant_id, tenant_config):

        brain_type = tenant_config["brain"]

        if brain_type == "healthcare":
            return HealthcareBrain()

        elif brain_type == "business":
            return BusinessBrain(tenant_id)

        else:
            raise Exception("Unknown brain type")
