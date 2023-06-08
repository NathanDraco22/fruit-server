from pydantic import BaseModel


class FruitModel(BaseModel):
    name: str
    color : str
    flavor : str
    calories: int
    description: str



