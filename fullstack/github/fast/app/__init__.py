from fastapi import FastAPI
from app.routes import router

# Create an instance of FastAPI
app = FastAPI()

# Include the router
app.include_router(router)
