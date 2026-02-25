from app.tenants.tenant_registry import TENANT_REGISTRY


class TenantManager:

    @staticmethod
    def get_tenant_config(tenant_id: str):

        config = TENANT_REGISTRY.get(tenant_id)

        if not config:
            raise Exception(f"Tenant not found: {tenant_id}")

        return config
