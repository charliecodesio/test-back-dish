 
from sqlalchemy.orm import Session
from . import models, schemas

def get_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_data: schemas.TaskCreate):
    task = get_task_by_id(db, task_id)
    print( f"Updating task {task_id} with data: {task_data}")
    if not task:
        return None
    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task