from sqlalchemy import Integer, String , Column
from . import Base 
from sqlalchemy.orm import relationship
class Languages(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key= True , index=True )
    ten_ngon_ngu = Column(String(100), nullable= False )
    
    problem_languages = relationship("ProblemLanguages", back_populates="language")
    submissions = relationship("Submissions", back_populates="language")