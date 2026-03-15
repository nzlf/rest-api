from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    tech_stack = Column(String(200), nullable=False)
    github_url = Column(String(255), nullable=True)
    demo_url = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)