from sqlalchemy import Integer,String , Column, ForeignKey , PrimaryKeyConstraint 
from sqlalchemy.orm import relationship 
from . import Base  
class ProblemLanguages(Base):
    __tablename__ = "problem_languages"
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable= False)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable= False)
    __table_args__ = (PrimaryKeyConstraint("problem_id","language_id"),)
    
    problem = relationship("Problems", back_populates="problem_languages")
    language = relationship("Languages", back_populates="problem_languages")