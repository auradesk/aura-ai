from abc import ABC, abstractmethod


class BaseDomain(ABC):
    """
    Base class for all Aura domains.
    Every domain must implement these methods.
    """

    @abstractmethod
    def shape_prompt(self, user_input: str) -> str:
        pass

    @abstractmethod
    def validate(self, user_input: str) -> None:
        pass

    @abstractmethod
    def post_process(self, response: str) -> str:
        pass
