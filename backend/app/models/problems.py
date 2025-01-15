from sqlalchemy import Integer, String, Column , ForeignKey ,DateTime
from sqlalchemy.orm import relationship 
from . import Base 
import datetime
from sqlalchemy.sql import func 
class problems(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key= True , index= True )
    tieu_de = Column(String(255), nullable= False)
    mo_ta = Column(String, nullable= False)
    difficulty_id = Column(Integer, ForeignKey("difficulties,id"), nullable= False)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable= True)
    nguoi_tao_id = Column(Integer, ForeignKey("users.id"),nullable= True)
    ngay_tao = Column(DateTime )
    ngay_cap_nhat = Column(DateTime, server_default= func.now(), onupdate= func.now())
    
    difficulty = relationship("difficulties", back_populates="problems")
    topic = relationship("topics", back_populates="problems")
    creator = relationship("users", back_populates="created_problems")
    problem_languages = relationship("problem_languages", back_populates="problem")
    contest_problems = relationship("contest_problems", back_populates="problem")
    submissions = relationship("submissions", back_populates="problem")
    testcases = relationship("testcases", back_populates="problem")
    discussions = relationship("discussions", back_populates="problem")