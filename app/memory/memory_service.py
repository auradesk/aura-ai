from sqlalchemy.orm import Session

from app.memory.memory_repository import MemoryRepository


class MemoryService:

    def __init__(self):

        self.repository = MemoryRepository()

    def store_memory(
        self,
        db: Session,
        tenant_id: str,
        domain: str,
        message: str,
        response: str
    ):

        return self.repository.save_memory(
            db=db,
            tenant_id=tenant_id,
            domain=domain,
            message=message,
            response=response
        )

    def get_recent_memories(
        self,
        db: Session,
        tenant_id: str
    ):

        return self.repository.get_recent_memories(
            db=db,
            tenant_id=tenant_id
        )
