import uvicorn
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class TaskSchema(BaseModel):
    id: str
    title: str
    is_completed: bool

tasks: list[TaskSchema] = []

class CreateTaskSchema(BaseModel):
    title: str
    is_completed: bool = False

class UpdateTaskSchema(BaseModel):
    title: str
    is_completed: bool

@app.get("/tasks", status_code=status.HTTP_200_OK)
def get_all_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: CreateTaskSchema):
    new_task = TaskSchema(id=str(uuid4()), title=task.title, is_completed=task.is_completed)
    tasks.append(new_task)

    return new_task

@app.patch("/tasks/{task_id}")
def update_task(task_id: str, new_task: UpdateTaskSchema):
    for task in tasks:
        if task.id == task_id:
            task.title = new_task.title
            task.is_completed = new_task.is_completed

            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача не найдена"
    )

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача не найдена"
    )



if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)