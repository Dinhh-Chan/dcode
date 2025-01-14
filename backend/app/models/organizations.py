from sqlalchemy import Integer, String, Column, Text 
from sqlalchemy.orm import relationship
from datetime import Date
from . import Base  
class orginations(Base):
    __tablename__ = "orginations"
    id =Column(Integer, primary_key= True , index= True )
    ten_to_chuc = Column(String(255), nullable= False )
    mo_ta = Column(Text)
    ngay_tao = Column(Date) 
    