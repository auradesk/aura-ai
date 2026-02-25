# app/engine/memory_reinforcement_engine.py

from datetime import datetime
from sqlalchemy.orm import Session

from app.db.memory_models import ConversationMemory

class MemoryReinforcementEngine:
    """
    Handles reinforcement learning for memory importance and confidence.
    """

    def __init__(self, db: Session):
        self.db = db

    # -----------------------------
    # Reinforce Memory
    # -----------------------------
    def reinforce_memory(self, memory_id: int, success: bool, importance_delta: float = 0.1,
                         confidence_delta: float = 0.05):
        """
        Adjusts importance and confidence of a memory based on success/failure.
        """
        memory = self.db.query(ConversationMemory).get(memory_id)
        if memory:
            # Reinforce if success
            if success:
                memory.importance += importance_delta
                memory.confidence += confidence_delta
            # Penalize if failure
            else:
                memory.importance = max(0.0, memory.importance - importance_delta)
                memory.confidence = max(0.0, memory.confidence - confidence_delta)

            memory.last_accessed = datetime.utcnow()
            self.db.commit()
            self.db.refresh(memory)
        return memory

    # -----------------------------
    # Decay Memory Over Time
    # -----------------------------
    def decay_memories(self, domain: str = None, decay_factor: float = 0.01):
        """
        Gradually decay importance of older memories to prioritize newer interactions.
        """
        query = self.db.query(ConversationMemory)
        if domain:
            query = query.filter_by(domain=domain)

        memories = query.all()
        for mem in memories:
            mem.importance = max(0.0, mem.importance - decay_factor)
        self.db.commit()
        return memories