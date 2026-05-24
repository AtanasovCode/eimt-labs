from fastapi import FastAPI
from contextlib import asynccontextmanager
from web.product_router import router as product_api_router
from web.cart_couter import router as cart_api_router
from database.seed import seed
from database.database import engine
from model.models import Base


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    seed()
    yield
    
app = FastAPI(lifespan=lifespan)
app.include_router(product_api_router)
app.include_router(cart_api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
