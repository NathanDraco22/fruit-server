from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.modules.fruits.router import fruits_router


app: FastAPI = FastAPI(
    title="Fruit Server"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(fruits_router.fruit_router, prefix= "/fruit")


