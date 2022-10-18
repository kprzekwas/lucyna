from fastapi import APIRouter, Depends, status

from app.schemas import GetTasks

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_tasks(command: GetTasks = Depends()):
    result = await get_tasks(command=command)

    return result


@router.post("/", status_code=status.HTTP_201_CREATED)
async def get_tasks(command: CreateTask):
    result = await get_tasks(command=command)

    return result
