
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

