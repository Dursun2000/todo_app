from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: str
    title: str
    is_completed: bool

class CreateTaskSchema(BaseModel):
    title: str
    is_completed: bool = False

class UpdateTaskSchema(BaseModel):
    title: str
    is_completed: bool