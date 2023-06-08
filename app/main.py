from fastapi import FastAPI
from app.modules.fruits.router import fruits_router

app: FastAPI = FastAPI(
    title="Fruit Server"
)

app.include_router(fruits_router.fruit_router, prefix= "/fruit")


