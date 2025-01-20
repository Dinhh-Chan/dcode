from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship 
from . import Base 
class Topics(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key= True , index= True)
    ten_chu_de = Column(String(100), nullable= False)
    
    problems = relationship("Problems", back_populates="topic")