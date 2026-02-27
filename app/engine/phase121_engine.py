# ============================================================
# AURA AI CORE — PHASE 121 ENGINE
# Cognitive Assessment Engine
# ============================================================

from datetime import datetime
import uuid


class Phase121Engine:

    def __init__(self):
        self.history = []

    def assess(self, input_data: dict):
        """
        Perform intelligent system assessment
        """

        assessment_id = str(uuid.uuid4())

        result = {
            "assessment_id": assessment_id,
            "timestamp": datetime.utcnow().isoformat(),
            "input": input_data,
            "cognitive_state": self._determine_state(input_data),
            "confidence": self._calculate_confidence(input_data),
            "recommendation": self._generate_recommendation(input_data)
        }

        self.history.append(result)

        return result

    def _determine_state(self, input_data):

        if not input_data:
            return "IDLE"

        if "critical" in str(input_data).lower():
            return "CRITICAL"

        if "warning" in str(input_data).lower():
            return "WARNING"

        return "STABLE"

    def _calculate_confidence(self, input_data):

        if not input_data:
            return 0.5

        size = len(str(input_data))

        if size > 100:
            return 0.95

        if size > 50:
            return 0.85

        return 0.75

    def _generate_recommendation(self, input_data):

        state = self._determine_state(input_data)

        if state == "CRITICAL":
            return "Immediate intervention required"

        if state == "WARNING":
            return "Monitor and review"

        if state == "STABLE":
            return "Continue normal operation"

        return "No action required"

    def get_history(self):

        return self.history