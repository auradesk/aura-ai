from app.adapters.factory import AdapterFactory
from app.telemetry.db_logger import log_usage
from app.memory.memory_service import MemoryService


class Orchestrator:

    def __init__(self):

        self.adapter_factory = AdapterFactory()

        self.memory_service = MemoryService()

    def handle_request(
        self,
        tenant_id: str,
        domain: str,
        message: str,
        tenant_config: dict,
        db
    ):

        adapter = self.adapter_factory.get_adapter(tenant_config)

        response = adapter.generate(
            tenant_id=tenant_id,
            domain=domain,
            message=message
        )

        # store memory
        self.memory_service.store_memory(
            db=db,
            tenant_id=tenant_id,
            domain=domain,
            message=message,
            response=response
        )

        # log telemetry
        log_usage(
            db=db,
            tenant_id=tenant_id,
            domain=domain
        )

        return response
