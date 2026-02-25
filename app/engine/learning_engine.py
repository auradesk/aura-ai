# app/engine/learning_engine.py

from app.engine.memory_engine import MemoryEngine

class LearningEngine:

    def __init__(self):
        self.memory = MemoryEngine()

    def execute(self, data: dict):

        goal = data.get("goal")
        step = data.get("step")
        success = data.get("success")

        if goal is None or step is None or success is None:
            return {
                "status": "error",
                "message": "goal, step, and success required"
            }

        # Learn
        self.memory.store_result(goal, step, success)

        # Assess decision confidence
        confidence = self.memory.get_confidence(goal)

        decision = "improve" if confidence < 0.7 else "continue"

        return {
            "status": "learning_complete",
            "goal": goal,
            "confidence": confidence,
            "decision": decision
        }