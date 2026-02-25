def get_tenant_config(tenant_id: str):

    configs = {

        "hospital_001": {
            "name": "City Hospital",
            "model_provider": "local"
        },

        "enterprise_001": {
            "name": "Enterprise Corp",
            "model_provider": "openai"
        }

    }

    return configs.get(
        tenant_id,
        {
            "name": "Default Tenant",
            "model_provider": "local"
        }
    )
