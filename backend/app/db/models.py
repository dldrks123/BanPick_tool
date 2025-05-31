# backend/app/db/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Champion(Base):
    __tablename__ = "champions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)    # 길이 100
    title = Column(String(200))                             # 길이 200

    banpicks = relationship("BanPick", back_populates="champion")

class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True, index=True)
    mode = Column(String(10))            # e.g., "BO3", "BO5"
    fearless_type = Column(String(10))   # "soft" or "hard"

    teams = relationship("Team", back_populates="match")
    banpicks = relationship("BanPick", back_populates="match")

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"))
    name = Column(String(100))           # 팀 이름
    side = Column(String(10))            # "blue" or "red"

    match = relationship("Match", back_populates="teams")
    banpicks = relationship("BanPick", back_populates="team")

class BanPick(Base):
    __tablename__ = "banpicks"
    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))
    order_index = Column(Integer)        # 밴/픽 순서
    action_type = Column(String(10))     # "BAN" 또는 "PICK"
    champion_id = Column(Integer, ForeignKey("champions.id"))

    match = relationship("Match", back_populates="banpicks")
    team = relationship("Team", back_populates="banpicks")
    champion = relationship("Champion", back_populates="banpicks")
