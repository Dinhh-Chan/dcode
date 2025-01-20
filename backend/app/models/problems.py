from sqlalchemy import Integer, String, Column , ForeignKey ,DateTime
from sqlalchemy.orm import relationship 
from . import Base 
import datetime
from sqlalchemy.sql import func 
class Problems(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key= True , index= True )
    tieu_de = Column(String(255), nullable= False)
    mo_ta = Column(String, nullable= False)
    difficulty_id = Column(Integer, ForeignKey("difficulties.id"), nullable= False)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable= True)
    nguoi_tao_id = Column(Integer, ForeignKey("users.id"),nullable= True)
    ngay_tao = Column(DateTime )
    ngay_cap_nhat = Column(DateTime, server_default= func.now(), onupdate= func.now())
    
    difficulty = relationship("Difficulties", back_populates="problems")
    topic = relationship("Topics", back_populates="problems")
    creator = relationship("Users", back_populates="created_problems")
    problem_languages = relationship("ProblemLanguages", back_populates="problem")
    contest_problems = relationship("ContestProblems", back_populates="problem")
    submissions = relationship("Submissions", back_populates="problem")
    testcases = relationship("Testcases", back_populates="problem")
    discussions = relationship("Discussions", back_populates="problem")