import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class TaskSchema(BaseModel):
    id: str
    title: str
    is_completed: bool

tasks: list[TaskSchema] = []

class CreateTaskSchema(BaseModel):
    title: str
    is_completed: bool

@app.get("/tasks", status_code=status.HTTP_200_OK)
def get_all_tasks():
    return tasks

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)