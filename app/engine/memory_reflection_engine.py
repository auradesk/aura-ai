# memory_reflection_engine.py

from datetime import datetime

class MemoryReflectionEngine:
    """
    Phase 42: Advanced Memory & Self-Reflection Engine
    Handles storing memories, retrieving them, and performing self-reflection.
    """

    def __init__(self):
        # In-memory storage (replace with DB later)
        self.memories = []

    def store_memory(self, context: str, result: str):
        """
        Store a memory with timestamp
        """
        memory_entry = {
            "timestamp": datetime.now(),
            "context": context,
            "result": result
        }
        self.memories.append(memory_entry)
        print(f"[Memory Stored] {memory_entry}")

    def retrieve_memories(self, limit=5):
        """
        Retrieve the most recent memories
        """
        return self.memories[-limit:]

    def reflect(self):
        """
        Perform simple self-reflection on recent memories
        """
        print("\n[Reflection Start]")
        recent_memories = self.retrieve_memories()
        reflections = []
        for mem in recent_memories:
            # Simple reflection: extract lessons from result
            lesson = f"Learned from '{mem['context']}': {mem['result']}"
            reflections.append(lesson)
            print(f"[Reflection] {lesson}")
        print("[Reflection End]\n")
        return reflections

# --------------------------
# Simple Test of Phase 42
# --------------------------
if __name__ == "__main__":
    engine = MemoryReflectionEngine()

    # Simulate storing memories
    engine.store_memory("Completed healthcare summary task", "Success")
    engine.store_memory("Analyzed AI reasoning logs", "Found optimization points")
    engine.store_memory("Reviewed previous reflection", "Identified gaps in memory")

    # Perform self-reflection
    engine.reflect()