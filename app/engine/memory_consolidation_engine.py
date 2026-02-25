from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.memory_models import ConversationMemory


class MemoryConsolidationEngine:

    def __init__(self):
        self.session: Session = SessionLocal()

    def consolidate_memories(self, tenant_id: str, domain: str):
        """
        Consolidates memories by strengthening important ones
        and weakening irrelevant ones.
        """

        memories = (
            self.session.query(ConversationMemory)
            .filter(
                ConversationMemory.tenant_id == tenant_id,
                ConversationMemory.domain == domain
            )
            .all()
        )

        strengthened = 0
        weakened = 0

        for memory in memories:

            score = (
                memory.importance * 0.5 +
                memory.confidence * 0.3 +
                (memory.recall_count * 0.2)
            )

            # Strengthen strong memories
            if score > 0.7:
                memory.importance = min(1.0, memory.importance + 0.05)
                memory.confidence = min(1.0, memory.confidence + 0.03)
                strengthened += 1

            # Weaken weak memories
            elif score < 0.3:
                memory.importance = max(0.0, memory.importance - 0.05)
                memory.confidence = max(0.0, memory.confidence - 0.03)
                weakened += 1

            memory.last_accessed = datetime.utcnow()

        self.session.commit()

        return {
            "strengthened": strengthened,
            "weakened": weakened,
            "total": len(memories),
            "timestamp": datetime.utcnow().isoformat()
        }