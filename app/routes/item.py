from fastapi import APIRouter

item_router = APIRouter(prefix="/items", tags=["items"])


@item_router.get("/")
async def read_items():
    return [{"item_id": "Foo"}, {"item_id": "Bar"}]
