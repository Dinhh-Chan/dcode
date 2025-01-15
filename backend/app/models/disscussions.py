from sqlalchemy import Integer, String, ForeignKey , Column, DateTime
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func 
from . import Base 
import datetime 
class discussions(Base):
    __tablename__ = "discussions"
    id = Column(Integer, primary_key= True, index= True)
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable= False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable= False)
    tieu_de = Column(String, nullable= False)
    noi_dung= Column(String, nullable= False)
    ngay_tao= Column(DateTime, server_default= func.now())
    
    problem = relationship("problems", back_populates="discussions")
    user = relationship("users", back_populates="discussions")
    comments = relationship("comments", back_populates="discussion")