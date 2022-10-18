from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app import api

app = FastAPI()

app.include_router(api.router)

# we will working on tampletes
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event():
    # await on_startup()
    pass


@app.get("/")
async def root():
    return "Welcome to my app to go swagger: localhost:*port*/docs"
