from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaskResult(Base):
    __tablename__ = "task_results"

    id = Column(String, primary_key=True)
    status = Column(String, nullable=False)
    result = Column(JSON)
