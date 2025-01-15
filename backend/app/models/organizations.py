from sqlalchemy import Integer, String, Column, Text , DateTime
from sqlalchemy.orm import relationship
from . import Base  
class orginations(Base):
    __tablename__ = "organizations"
    id =Column(Integer, primary_key= True , index= True )
    ten_to_chuc = Column(String(255), nullable= False )
    mo_ta = Column(Text)
    ngay_tao = Column(DateTime) 
    
    users = relationship("users", back_populates="organization")
    contests = relationship("contests", back_populates="organization")