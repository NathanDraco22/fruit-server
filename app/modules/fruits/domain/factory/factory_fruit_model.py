
from ..dto.create_dto import CreateFruitDTO
from ..model.fruit_model import FruitModel

class FactoryFruitModel:

    @classmethod
    def fromJsonDict(cls, json: dict) -> FruitModel :
        return FruitModel(
            name        = json["name"],
            color       = json["color"],
            flavor      = json["flavor"],
            calories    = json["calories"],
            description = json["description"]
        )
    
    @classmethod
    def create_fruit_json(cls, create_dto: CreateFruitDTO) -> dict:
        data_dict = {
            "name" : create_dto.name,
            "color" : create_dto.color,
            "flavor" : create_dto.flavor,
            "calories" : create_dto.calories,
            "description" : create_dto.description
        }
        return data_dict