from fastapi import APIRouter, Path, Body
from ..domain import FruitRepository, FruitModel, CreateFruitDTO
from ..service.db_services import DBSimulate

fruit_router : APIRouter = APIRouter()
repo : FruitRepository = FruitRepository(db= DBSimulate() )

@fruit_router.get("", response_model= list[FruitModel])
async def get_all_fruits():
    return repo.get_all_fruits()


@fruit_router.get("/{id}", response_model=FruitModel)
async def get_by_id(id: int = Path()):
    return repo.get_fruit_by_id(id)

@fruit_router.post("", response_model=FruitModel)
async def create_fruit(body: CreateFruitDTO ):
    return repo.create_fruit(body)

@fruit_router.delete("/{id}")
async def delete_fruit(id: int = Path()):
    return repo.delete_fruit(id)



