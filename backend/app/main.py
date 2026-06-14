from fastapi import FastAPI

from app.database import Base, engine

from app.routes.rou import router as auth_router
from app.routes.task import router as task_router

app = FastAPI()

# Create Tables
Base.metadata.create_all(bind=engine)

# Register Routes
app.include_router(auth_router)
app.include_router(task_router)


@app.get("/")
def home():

    return {
        "message": "Backend Working"
    }