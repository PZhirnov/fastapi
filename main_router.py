from typing import Union
from fastapi import APIRouter
from datetime import datetime

from users.view import router_users

router = APIRouter()


@router.get("/")
def read_root():
    print(datetime.now())
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id, q: Union[str, None] = None):
    print(item_id)
    return {"item_id": item_id, "q": q}

