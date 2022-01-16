from fastapi import APIRouter

router_items = APIRouter()


@router_items.get("/items/", tags=["items"])
async def read_users():
    return [{"items": "Rick"}, {"items": "Morty"}]


@router_items.get("/items/me", tags=["items"])
async def read_user_me():
    return {"items": "fakecurrentuser"}


@router_items.get("/items/{items}", tags=["items"])
async def read_user(username: str):
    return {"items": username}
