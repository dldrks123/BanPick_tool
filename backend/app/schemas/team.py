# backend/app/schemas/team.py

from pydantic import BaseModel

class TeamBase(BaseModel):
    match_id: int
    name: str
    side: str            # "blue" or "red"

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True
