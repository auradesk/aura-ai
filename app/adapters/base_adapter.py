from abc import ABC, abstractmethod


class BaseAdapter(ABC):

    @abstractmethod
    def generate(
        self,
        tenant_id: str,
        domain: str,
        message: str
    ):
        pass
