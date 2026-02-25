from app.domains.healthcare.healthcare_engine import HealthcareEngine


class HealthcareBrain:

    def __init__(self):
        self.engine = HealthcareEngine()

    def think(self, message, memory_context):

        response = self.engine.process(message)

        return response
