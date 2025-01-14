from sqlalchemy import Integer, String, Column, ForeignKey 
import datetime
from sqlalchemy.sql import func 
from . import Base 
class contests(Base):
    id = Column(Integer, primary_key= True , index= True )
    ten_cuoc_thi = Column(String(255), nullable= False)
    thoi_gian_bat_dau = Column(datetime, nullable= False)
    thoi_gian_ket_thuc= Column(datetime, nullable= False)
    nguoi_tao_id = Column(Integer, ForeignKey("users.id"),nullable= True)
    to_chuc_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    ngay_tao =Column(datetime)