from fastapi import APIRouter

# Create a router instance
router = APIRouter()

# Example route
@router.get("/")
async def read_root():
    return {"Hello": "World"}

# Example dynamic route
@router.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
