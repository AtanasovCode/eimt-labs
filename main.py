from fastapi import FastAPI
from web.product_router import router as product_api_router


app = FastAPI()
app.include_router(product_api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
