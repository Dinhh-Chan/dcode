from sqlalchemy import Integer , Column ,ForeignKey, PrimaryKeyConstraint 
from . import Base 
from sqlalchemy.orm import relationship 
import datetime 
from sqlalchemy.sql import func 
class contest_participants(Base):
    __tablename__= "contest_participants"
    contest_id = Column(Integer, ForeignKey("contests.id"), nullable= False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable= False)
    diem = Column(Integer, default= 0)
    thoi_gian_tha_gia = Column(datetime, server_default= func.now())
    __table_args__= (PrimaryKeyConstraint("contest_id", "user_id"))