def build_intelligence_prompt(
    tenant_id: str,
    domain: str,
    user_message: str,
    memory_context: str
):
    """
    Builds the full intelligence prompt for Aura.
    """

    system_identity = (
        "You are Aura, an advanced multi-tenant artificial intelligence system.\n"
        "You remember past conversations and provide intelligent, helpful responses.\n"
        "You adapt based on tenant and domain.\n\n"
    )

    tenant_context = f"Tenant: {tenant_id}\n"
    domain_context = f"Domain: {domain}\n\n"

    memory_section = ""

    if memory_context:
        memory_section = (
            "Relevant Memory:\n"
            f"{memory_context}\n"
        )

    user_section = (
        "User Message:\n"
        f"{user_message}\n\n"
    )

    instructions = (
        "Provide a helpful, intelligent, and context-aware response."
    )

    prompt = (
        system_identity +
        tenant_context +
        domain_context +
        memory_section +
        user_section +
        instructions
    )

    return prompt
