from pydantic import BaseModel


class CreateFruitDTO(BaseModel):
    name: str
    color : str
    flavor : str
    calories: int
    description: str





