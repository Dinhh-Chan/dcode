from sqlalchemy import Integer, String, ForeignKey, PrimaryKeyConstraint , Column 
from sqlalchemy import relationship 
from . import Base 
class course_problems(Base):
    __tablename__= "course_problems"
    course_id = Column(Integer, ForeignKey("courses.id"), nullable= False )
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable= False)
    __table_args__= (PrimaryKeyConstraint("course_id", "problem_id"))