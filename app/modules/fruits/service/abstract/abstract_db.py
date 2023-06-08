from abc import ABC, abstractmethod

class DBServices(ABC):

    @abstractmethod
    def fetch_all(self) -> list[dict]:
        pass
    @abstractmethod
    def fetch_by_id(self,id:int) -> dict:
        pass




