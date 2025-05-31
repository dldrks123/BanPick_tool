# backend/app/crud/match.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Match as MatchModel
from app.schemas.match import MatchCreate

async def get_match(db: AsyncSession, match_id: int):
    result = await db.execute(
        select(MatchModel).where(MatchModel.id == match_id)
    )
    return result.scalars().first()

async def get_matches(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(
        select(MatchModel).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def create_match(db: AsyncSession, match: MatchCreate):
    db_match = MatchModel(mode=match.mode, fearless_type=match.fearless_type)
    db.add(db_match)
    await db.commit()
    await db.refresh(db_match)
    return db_match
