from app.domains.healthcare.domain import HealthcareDomain


class DomainRegistry:

    _domains = {
        "healthcare": HealthcareDomain
    }

    @classmethod
    def get(cls, domain_name: str):
        domain_class = cls._domains.get(domain_name)

        if not domain_class:
            raise ValueError(f"Unsupported domain: {domain_name}")

        return domain_class()
