from sqlalchemy import Integer, String, Column
from sqlalchemy import relationship 
from . import Base 
class topics(Base):
    id = Column(Integer, primary_key= True , index= True)
    ten_chu_de = Column(String(100), nullable= False)