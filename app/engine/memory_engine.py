# app/engine/memory_engine.py

class MemoryEngine:

    def __init__(self):
        self.memory = {}

    def store_result(self, goal, step, success):

        if goal not in self.memory:
            self.memory[goal] = {
                "success": 0,
                "total": 0
            }

        self.memory[goal]["total"] += 1

        if success:
            self.memory[goal]["success"] += 1

    def get_confidence(self, goal):

        if goal not in self.memory:
            return 0.0

        data = self.memory[goal]

        if data["total"] == 0:
            return 0.0

        return data["success"] / data["total"]