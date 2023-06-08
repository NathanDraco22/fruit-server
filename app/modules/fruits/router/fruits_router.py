from fastapi import APIRouter, Path
from ..domain.fruits_repository import FruitRepository, FruitModel
from ..service.db_services import DBSimulate

fruit_router : APIRouter = APIRouter()
repo : FruitRepository = FruitRepository(db= DBSimulate() )

@fruit_router.get("", response_model= list[FruitModel])
async def get_all_fruits():
    return repo.get_all_fruits()


@fruit_router.get("/{id}")
async def get_by_id(id: int = Path()):
    return repo.get_by_id(id)


@fruit_router.delete("/{id}")
async def delete_fruit(id: int = Path()):
    return repo.delete_fruit(id)



