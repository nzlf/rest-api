from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.routers.projects import router as project_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio REST API",
    description="API sederhana untuk menyimpan project portofolio",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to Portfolio REST API"}

app.include_router(project_router)