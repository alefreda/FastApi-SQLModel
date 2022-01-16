from fastapi import Depends, FastAPI

from dependencies import CommonQueryParams, CommonQueryParams2
from routers import users, items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router_items)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items33/")
async def read_items(commons: CommonQueryParams = Depends()):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response


@app.get("/items44/")
async def read_items(commons: CommonQueryParams2 = Depends()):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({"items": items})
    return response
