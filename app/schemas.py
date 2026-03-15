from datetime import datetime
from typing import Optional
from pydantic import BaseModel, HttpUrl

class ProjectCreate(BaseModel):
    title: str
    description: str
    tech_stack: str
    github_url: Optional[HttpUrl] = None
    demo_url: Optional[HttpUrl] = None

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    tech_stack: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    demo_url: Optional[HttpUrl] = None

class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    tech_stack: str
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True