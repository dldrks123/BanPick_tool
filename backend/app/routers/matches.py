# backend/app/routers/matches.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.match import Match, MatchCreate
from app.crud.match import get_match, get_matches, create_match
from app.db.session import get_db

router = APIRouter(prefix="/matches", tags=["matches"])

@router.post("/", response_model=Match)
async def create_match_endpoint(
    match: MatchCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_match(db, match)

@router.get("/", response_model=List[Match])
async def read_matches(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
):
    return await get_matches(db, skip, limit)

@router.get("/{match_id}", response_model=Match)
async def read_match(
    match_id: int,
    db: AsyncSession = Depends(get_db),
):
    db_match = await get_match(db, match_id)
    if not db_match:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match
