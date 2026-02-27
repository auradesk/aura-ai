from sqlalchemy.orm import Session
from app.memory.memory_models import AuraMemory


class MemoryEngine:

    def store_memory(
        self,
        db: Session,
        organization_id: str,
        memory_type: str,
        content: str
    ):

        memory = AuraMemory(
            organization_id=organization_id,
            memory_type=memory_type,
            content=content
        )

        db.add(memory)
        db.commit()
        db.refresh(memory)

        return memory


    def get_memories(
        self,
        db: Session,
        organization_id: str
    ):

        return db.query(AuraMemory).filter(
            AuraMemory.organization_id == organization_id
        ).all()


memory_engine = MemoryEngine()