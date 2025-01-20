from sqlalchemy import Integer, String, Enum, ForeignKey, Column , Float, DateTime
from sqlalchemy.orm import relationship
import datetime
from . import Base
from .enums import SubmissionStatusEnum
from sqlalchemy.sql import func 
class Submissions(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key= True, index= True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable= False)
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable= False)
    code = Column(String, nullable= False)
    language_id = Column(Integer,ForeignKey("languages.id"), nullable= False)
    status = Column(Enum(SubmissionStatusEnum), default=SubmissionStatusEnum.Pending)
    thoi_gian_nop = Column(DateTime, server_default= func.now())
    thoi_gian_thuc_hien = Column(Float )
    dung_luong_bo_nho = Column(Integer)
    contest_id = Column(Integer, ForeignKey("contests.id"))
    diem= Column(Integer, default=0)
    
    user = relationship("Users", back_populates="submissions")
    problem = relationship("Problems", back_populates="submissions")
    language = relationship("Languages", back_populates="submissions")
    contest = relationship("Contests")