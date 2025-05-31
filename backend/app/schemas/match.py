# backend/app/schemas/match.py

from pydantic import BaseModel
from typing import Optional

class MatchBase(BaseModel):
    mode: str              # e.g., "BO3", "BO5"
    fearless_type: str     # "soft" or "hard"

class MatchCreate(MatchBase):
    pass

class Match(MatchBase):
    id: int

    class Config:
        orm_mode = True
