
from .model.fruit_model import FruitModel
from .factory.factory_fruit_model import FactoryFruitModel
from ..service.abstract.abstract_db import DBServices
from .abstract.abstract_fruit_repo import FruitRepo

class FruitRepository(FruitRepo):
    db: DBServices

    def __init__(self, db: DBServices):
        self.db = db
        pass


    def get_all_fruits(self) -> list[FruitModel]:
        raw_data = self.db.fetch_all()
        models = []
        for data in raw_data:
            model = FactoryFruitModel.fromJsonDict(json= data)
            models.append(model)
        return models
    
    def get_fruit_by_id(self, id : int):
        res = self.db.fetch_by_id(id=id)
        model = FactoryFruitModel.fromJsonDict(res)
        return model
    
    def delete_fruit(self, id: int) -> bool:
        return True