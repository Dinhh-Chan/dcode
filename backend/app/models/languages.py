from sqlalchemy import Integer, String , Column
from . import Base 
class languages(Base):
    ___tablename__= "languages"
    id = Column(Integer, primary_key= True , index=True )
    ten_ngon_ngu = Column(String(100), nullable= False )
    