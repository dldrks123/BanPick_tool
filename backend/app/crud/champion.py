# backend/app/crud/champion.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Champion as ChampionModel
from app.schemas.champion import ChampionCreate

async def get_champion(db: AsyncSession, champion_id: int):
    result = await db.execute(
        select(ChampionModel).where(ChampionModel.id == champion_id)
    )
    return result.scalars().first()

async def get_champions(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(ChampionModel).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def create_champion(db: AsyncSession, champion: ChampionCreate):
    db_champion = ChampionModel(name=champion.name, title=champion.title)
    db.add(db_champion)
    await db.commit()
    await db.refresh(db_champion)
    return db_champion
