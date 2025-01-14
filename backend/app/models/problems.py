from sqlalchemy import Integer, String, Column , ForeignKey 
from sqlalchemy import relationship 
from . import Base 
from datetime import Date 
import datetime
from sqlalchemy.sql import func 
class problems(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key= True , index= True )
    tieu_de = Column(String(255), nullable= False)
    mo_ta = Column(String, nullable= False)
    difficulty_id = Column(Integer, ForeignKey("difficulties,id"), nullable= False)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable= True)
    nguoi_tao_id = Column(Integer, ForeignKey("users.id"),nullable= True)
    ngay_tao = Column(datetime )
    ngay_cap_nhat = Column(datetime, server_default= func.now(), onupdate= func.now())