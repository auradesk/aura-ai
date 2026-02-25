# agi_engine.py
from app.engine.memory_engine import MemoryEngine
from app.engine.learning_engine import LearningEngine

class AGIEngine:
    """
    Core AGI Engine.
    Manages memory, learning, and higher-level reasoning.
    """

    def __init__(self, memory_engine: MemoryEngine, learning_engine: LearningEngine):
        self.memory_engine = memory_engine
        self.learning_engine = learning_engine
        # You can add more modules like reasoning, reflection, etc.
        self.status = "initialized"

    def process_input(self, input_text: str):
        """
        Main method to process incoming text.
        """
        # Step 1: Store in memory
        self.memory_engine.store(input_text)

        # Step 2: Run learning / analysis
        learned_output = self.learning_engine.analyze(input_text)

        # Step 3: Generate response or summary
        response = f"Processed: {learned_output}"

        return response

    def summarize_memory(self):
        """
        Returns a summary of recent memories.
        """
        memories = self.memory_engine.retrieve_recent()
        return f"Memory Summary: {memories}"