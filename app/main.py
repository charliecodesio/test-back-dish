
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks", response_model=list[schemas.Task])
def get_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")
    return tasks

@app.get("/tasks/{id}", response_model=schemas.Task)
def get_task_by_id(id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_task(db, task)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating task: {str(e)}")

@app.put("/tasks/{id}", response_model=schemas.Task)
def update_task(id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{id}", response_model=schemas.Task)
def delete_task(id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task

