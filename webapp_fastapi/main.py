import pathlib
from typing import Union

from fastapi import FastAPI

app = FastAPI()


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


@app.get("/")
def read_root(order_id:str=None):
    print(order_id)
    return {"Hello": "World", "BASE_DIR": BASE_DIR}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/about")
async def read_about():
    return {"Hello": "World"}
