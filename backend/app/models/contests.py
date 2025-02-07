from sqlalchemy import Integer, String, Column, ForeignKey , DateTime, Text
import datetime
from sqlalchemy.sql import func 
from . import Base 
from sqlalchemy.orm import relationship
class Contests(Base):
    __tablename__ = "contests"
    id = Column(Integer, primary_key=True, index=True)
    ten_cuoc_thi = Column(String(255), nullable=False)
    mo_ta = Column(Text)
    thoi_gian_bat_dau = Column(DateTime, nullable=False)
    thoi_gian_ket_thuc = Column(DateTime, nullable=False)
    nguoi_tao_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    ngay_tao = Column(DateTime, server_default=func.now())
    
    creator = relationship("Users", back_populates="created_contests")
    organization = relationship("Organizations", back_populates="contests")
    contest_problems = relationship("ContestProblems", back_populates="contest")
    contest_participants = relationship("ContestParticipants", back_populates="contest")
