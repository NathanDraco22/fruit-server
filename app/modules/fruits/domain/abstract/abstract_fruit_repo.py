from abc import ABC, abstractmethod
from ..model.fruit_model import FruitModel


class FruitRepo(ABC):

    @abstractmethod
    def get_all_fruits(self) -> list[FruitModel]:
        pass

    @abstractmethod
    def get_fruit_by_id(self,id:int) -> FruitModel:
        pass

    @abstractmethod
    def delete_fruit(self,id:int) -> bool:
        pass



