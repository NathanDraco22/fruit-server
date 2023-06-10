from ..service.abstract.abstract_db import DBServices
from . import *
from rich.console import Console

console = Console()

class FruitRepository(FruitRepo):
    db: DBServices

    def __init__(self, db: DBServices):
        self.db = db
        pass

    def create_fruit(self,create_dto: CreateFruitDTO) -> FruitModel:
        json_dict = FactoryFruitModel.create_fruit_json(create_dto)
        resp = self.db.create(json_dict)
        return FactoryFruitModel.fromJsonDict(resp)

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
        return self.db.delete(id=id)