from fastapi import FastAPI
from api.routers import user, ai_generation

app = FastAPI()

app.include_router(user.router)

app.include_router(ai_generation.router, prefix="/ai", tags=["AI Core"])
