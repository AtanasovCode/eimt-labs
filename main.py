from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from web.product_router import router as product_api_router
from web.category_router import router as category_api_router
from web.manufacturer_router import router as manufacturer_api_router
from web.cart_router import router as cart_api_router
from database.seed import seed
from database.database import engine
from model.models import Base


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    seed()
    yield
    
app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_api_router)
app.include_router(cart_api_router)
app.include_router(category_api_router)
app.include_router(manufacturer_api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
