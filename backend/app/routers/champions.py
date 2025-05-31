# backend/app/routers/champions.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.champion import Champion, ChampionCreate
from app.crud.champion import get_champion, get_champions, create_champion
from app.db.session import get_db

router = APIRouter(prefix="/champions", tags=["champions"])

@router.post("/", response_model=Champion)
async def create_champion_endpoint(
    champion: ChampionCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_champion(db, champion)

@router.get("/", response_model=List[Champion])
async def read_champions(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    return await get_champions(db, skip, limit)

@router.get("/{champion_id}", response_model=Champion)
async def read_champion(
    champion_id: int,
    db: AsyncSession = Depends(get_db),
):
    db_champ = await get_champion(db, champion_id)
    if not db_champ:
        raise HTTPException(status_code=404, detail="Champion not found")
    return db_champ
