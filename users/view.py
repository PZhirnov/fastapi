from fastapi import APIRouter

router_users = APIRouter()


@router_users.get("/users")
def read_root():
    print('пользователи')
    return {"users": "Пользователи"}
