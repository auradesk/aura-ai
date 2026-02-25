from .tenant_config import TenantConfig

TENANTS = {
    "hospital_001": TenantConfig(
        tenant_id="hospital_001",
        adapter="local",
        plan="enterprise"
    ),
    "school_001": TenantConfig(
        tenant_id="school_001",
        adapter="local",
        plan="basic"
    ),
    "startup_001": TenantConfig(
        tenant_id="startup_001",
        adapter="openai",
        plan="pro"
    ),
}

def get_tenant_config(tenant_id: str) -> TenantConfig:
    return TENANTS.get(tenant_id)
