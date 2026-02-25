from .base_domain import BaseDomain


class HealthcareDomain(BaseDomain):
    """
    Healthcare-specific behavior layer.
    Adds medical-safe prompting and compliance awareness.
    """

    def validate(self, user_input: str) -> None:
        """
        Basic validation rules.
        You can later expand this with PHI detection.
        """
        if len(user_input.strip()) == 0:
            raise ValueError("Healthcare input cannot be empty.")

    def shape_prompt(self, user_input: str) -> str:
        """
        Wrap the user prompt with healthcare-safe context.
        """

        system_context = """
You are Aura Healthcare Assistant.
Provide medically informative but non-diagnostic responses.
Always include:
- A disclaimer that this is not medical advice.
- Encourage consulting a licensed professional.
- Avoid prescribing medication or dosages.
Be clear, calm, and professional.
        """

        return f"{system_context}\n\nUser Query:\n{user_input}"

    def post_process(self, response: str) -> str:
        """
        Add healthcare disclaimer at the end if not present.
        """

        disclaimer = "\n\n⚠️ This information is for educational purposes only and does not replace professional medical advice."

        if "educational purposes" not in response:
            response += disclaimer

        return response
