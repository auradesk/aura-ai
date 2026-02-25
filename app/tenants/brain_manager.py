# app/tenants/brain_manager.py

class BrainManager:

    def __init__(self):

        self.active_brains = {}


    def get_brain(self, tenant_id):

        if tenant_id not in self.active_brains:

            self.active_brains[tenant_id] = {
                "tenant_id": tenant_id,
                "memory_loaded": True,
                "knowledge_loaded": True,
                "vector_loaded": True
            }

        return self.active_brains[tenant_id]


brain_manager = BrainManager()
