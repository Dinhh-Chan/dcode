from sqlalchemy import Integer, String , Column , ForeignKey 
from . import Base 
import datetime 
from sqlalchemy.sql import func 
class coures(Base):
    id = Column(Integer,primary_key= True, index=True)
    ten_khoa_hoc = Column(String(255), nullable= False)
    mo_ta = Column(String)
    ngay_tao = Column(datetime, server_default= func.now())
    nguoi_tao_id = Column(Integer, ForeignKey("users.id"))
    
