from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import hello

app = FastAPI(
    title="My FastAPI Backend",
    description="An API with auto-generated Swagger UI",
    version="1.0.0"
)

# List of allowed origins (e.g., your Vite frontend at localhost:5173)
origins = [
    "http://localhost:3000",  # Frontend is on port 3000
    # Add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],       # or restrict to specific methods: ["GET", "POST"]
    allow_headers=["*"],       # or restrict to specific headers
)

app.include_router(hello.router, prefix="/api")
