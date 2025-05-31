# backend/app/main.py

from fastapi import FastAPI
from app.db.session import engine
from app.db.models import Base
from app.routers.champions import router as champions_router
from app.routers.matches import router as matches_router

app = FastAPI()

app.include_router(champions_router)
app.include_router(matches_router)

@app.on_event("startup")
async def on_startup():
    # 데이터베이스에 테이블이 없으면 생성
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def read_root():
    return {"message": "Hello, LoL Ban & Pick!"}
