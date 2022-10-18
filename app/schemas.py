from datetime import date

from pydantic import BaseModel


class GetTasks(BaseModel):
    pass


class CreateTask(BaseModel):
    description: str


class TaskResult(BaseModel):
    id: int
    description: str
    date: date
