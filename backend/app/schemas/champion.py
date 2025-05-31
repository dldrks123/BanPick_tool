# backend/app/schemas/champion.py

from pydantic import BaseModel

# 1) 공통 속성
class ChampionBase(BaseModel):
    name: str
    title: str

# 2) 생성 시 사용하는 스키마
class ChampionCreate(ChampionBase):
    pass

# 3) 조회 응답용 스키마 (id 포함)
class Champion(ChampionBase):
    id: int

    class Config:
        orm_mode = True
