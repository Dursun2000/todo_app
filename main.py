import uvicorn
from fastapi import FastAPI
from app.endpoints.task_views.task import router as task_router
app = FastAPI()
app.include_router(task_router)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)