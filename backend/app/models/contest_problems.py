from sqlalchemy import Integer, ForeignKey, PrimaryKeyConstraint , Column
from sqlalchemy.orm import relationship
from . import Base 
class contest_problems(Base):
    __tablename__= "contest_problems"
    contest_id = Column(Integer, ForeignKey("contests.id"), nullable= False )
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable= False)
    __table_args__=  (PrimaryKeyConstraint("contest_id", "problem_id"),)
    
    contest = relationship("contests", back_populates="contest_problems")
    problem = relationship("problems")