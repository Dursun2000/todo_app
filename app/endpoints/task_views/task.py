from fastapi import APIRouter, status, HTTPException
from ...database import db
from ..task_views import schemas

from uuid import uuid4

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", status_code=status.HTTP_200_OK)
def get_all_tasks():
    return db.tasks

@router.post("/tasks")
def create_task(task: schemas.CreateTaskSchema):
    new_task = schemas.TaskSchema(id=str(uuid4()), title=task.title, is_completed=task.is_completed)
    db.tasks.append(new_task)

    return new_task

@router.patch("/tasks/{task_id}")
def update_task(task_id: str, new_task: schemas.UpdateTaskSchema):
    for task in db.tasks:
        if task.id == task_id:
            task.title = new_task.title
            task.is_completed = new_task.is_completed

            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача не найдена"
    )

@router.delete("{task_id}")
def delete_task(task_id: str):
    for task in db.tasks:
        if task.id == task_id:
            db.tasks.remove(task)
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача не найдена"
    )