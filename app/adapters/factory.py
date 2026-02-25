# Adapter Factory
# Selects the correct intelligence adapter for each tenant


# Import adapters
from app.adapters.local_adapter import LocalAdapter
from app.adapters.openai_adapter import OpenAIAdapter


# Tenant adapter mapping
TENANT_ADAPTER_MAP = {

    # Healthcare uses Local Intelligence (safe, offline)
    "hospital_001": "local",

    # Enterprise uses Cloud Intelligence (OpenAI when available)
    "enterprise_001": "openai",

    # Default fallback
    "default": "local"
}


def get_adapter(tenant_id: str):
    """
    Returns the correct adapter based on tenant configuration
    """

    adapter_type = TENANT_ADAPTER_MAP.get(
        tenant_id,
        TENANT_ADAPTER_MAP["default"]
    )

    if adapter_type == "openai":
        return OpenAIAdapter()

    return LocalAdapter()
