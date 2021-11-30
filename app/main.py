from fastapi import FastAPI

from app.api.views import router

app = FastAPI()
app.include_router(router)
