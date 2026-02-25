class HealthcareDomain:
    def __init__(self):
        self.name = "healthcare"

    def validate(self, message: str):
        if not message or len(message.strip()) == 0:
            raise ValueError("Healthcare message cannot be empty.")

    def shape_prompt(self, tenant_id: str, message: str) -> str:
        return f"""
You are Aura, an intelligent healthcare assistant.

Guidelines:
- Provide general educational medical information.
- Do NOT diagnose.
- Do NOT prescribe medication.
- Encourage seeking professional medical care when needed.

Tenant: {tenant_id}

User message:
{message}
"""

    def post_process(self, response: str) -> str:
        disclaimer = "\n\n⚠️ This information is for educational purposes only and is not medical advice."
        return response.strip() + disclaimer
