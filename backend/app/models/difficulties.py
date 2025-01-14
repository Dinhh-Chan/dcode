from sqlalchemy import Integer, String , Column , Enum
from sqlalchemy.orm import relationship 
from . import Base 
from emun import DiffycultyEnum 
class difficulties(Base):
    __tablename__= "difficulties"
    id = Column(Integer, primary_key= True, index= True)
    do_kho = Column(Enum(DiffycultyEnum), default= DiffycultyEnum.Easy)
    