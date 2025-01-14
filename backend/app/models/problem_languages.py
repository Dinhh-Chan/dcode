from sqlalchemy import Integer,String , Column, ForeignKey , PrimaryKeyConstraint 
from sqlalchemy import relationship 
from . import Base  
class problem_languages(Base):
    __tablename__ = "problem_languages"
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable= False)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable= False)
    __table_args__ = (PrimaryKeyConstraint("problem_id","language_id"))