import uvicorn
from fastapi import FastAPI, status
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

@app.get("/tasks", status_code=status.HTTP_200_OK)
def get_all_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: CreateTaskSchema):
    new_task = TaskSchema(id=str(uuid4()), title=task.title, is_completed=task.is_completed)
    tasks.append(new_task)

    return new_task

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)