from app.adapters.factory import get_adapter


class BusinessBrain:

    def __init__(self, tenant_id):
        self.adapter = get_adapter(tenant_id)
        self.tenant_id = tenant_id

    def think(self, domain, message, memory_context):

        response = self.adapter.generate(
            self.tenant_id,
            domain,
            message,
            memory_context
        )

        return response
