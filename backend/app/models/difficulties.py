from sqlalchemy import Integer, String , Column , Enum
from sqlalchemy.orm import relationship 
from . import Base 
from .enums import DiffycultyEnum 
class Difficulties(Base):
    __tablename__ = "difficulties"
    id = Column(Integer, primary_key= True, index= True)
    do_kho = Column(Enum(DiffycultyEnum, name="difficultyenum", create_type=False), default=DiffycultyEnum.Easy)
    
    problems = relationship("Problems", back_populates="difficulty")