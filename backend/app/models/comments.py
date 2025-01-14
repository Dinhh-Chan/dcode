from sqlalchemy import Integer, String, ForeignKey, Column 
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func 
import datetime 
from . import Base 
class comments(Base):
    id = Column(Integer, primary_key= True, index= True)
    discussion_id = Column(Integer, ForeignKey("discussions.id"), nullable= False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable= False)
    noi_dung = Column(String, nullable= False)
    ngay_tao = Column(datetime, server_default= func.now())