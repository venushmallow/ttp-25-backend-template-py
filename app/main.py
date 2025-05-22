from fastapi import FastAPI
from app.routers import hello

app = FastAPI(
    title="My FastAPI Backend",
    description="An API with auto-generated Swagger UI",
    version="1.0.0"
)

app.include_router(hello.router, prefix="/api")
