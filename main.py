from typing import Union

from fastapi import FastAPI
from datetime import datetime
from users.view import router_users

app = FastAPI()


@app.get("/")
def read_root():
    print(datetime.now())
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id, q: Union[str, None] = None):
    print(item_id)
    return {"item_id": item_id, "q": q}

app.include_router(router_users)
