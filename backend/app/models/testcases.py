from sqlalchemy import Integer, String , ForeignKey , Column , Float
from sqlalchemy.orm import relationship
from . import Base 
import datetime
from sqlalchemy.sql import func 
class testcases(Base):
    __tablename__ = "testcases"
    id = Column(Integer, primary_key= True, index= True)
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable= False)
    input_data = Column(String, nullable= False)
    output_data = Column(String, nullable= False)
    time_limit = Column(Float)    
    memory_limit = Column(Integer)