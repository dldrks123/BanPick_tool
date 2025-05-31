# backend/app/schemas/banpick.py

from pydantic import BaseModel

class BanPickBase(BaseModel):
    match_id: int
    team_id: int
    order_index: int
    action_type: str      # "BAN" or "PICK"
    champion_id: int

class BanPickCreate(BanPickBase):
    pass

class BanPick(BanPickBase):
    id: int

    class Config:
        orm_mode = True
