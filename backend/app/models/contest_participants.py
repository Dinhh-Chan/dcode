from sqlalchemy import Boolean, Integer , Column ,ForeignKey, PrimaryKeyConstraint , DateTime
from . import Base 
from sqlalchemy.orm import relationship 
import datetime 
from sqlalchemy.sql import func 
class ContestParticipants(Base):
    __tablename__ = "contest_participants"
    contest_id = Column(Integer, ForeignKey("contests.id"), nullable= False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable= False)
    diem = Column(Integer, default= 0)
    thoi_gian_tha_gia = Column(DateTime, server_default= func.now())
    approved = Column(Boolean, default=False)
    __table_args__= (PrimaryKeyConstraint("contest_id", "user_id"),)
    
    contest = relationship("Contests", back_populates="contest_participants")
    user = relationship("Users", back_populates="contest_participants")