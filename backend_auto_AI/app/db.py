from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, TaskResult
import os
DATABASE_URL = os.getenv("DATABASE_URL")

gine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=gine)

Base.metadata.create_all(bind=gine)

def get_task_result(task_id):
    session = SessionLocal()
    result = session.query(TaskResult).filter(TaskResult.id == task_id).first()
    session.close()
    return result.result if result else None