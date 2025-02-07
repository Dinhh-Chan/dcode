from sqlalchemy import Integer, String, ForeignKey, Column ,DateTime
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func 
import datetime 
from . import Base 
class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key= True, index= True)
    discussion_id = Column(Integer, ForeignKey("discussions.id"), nullable= False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable= False)
    noi_dung = Column(String, nullable= False)
    ngay_tao = Column(DateTime, server_default= func.now())
    
    discussion = relationship("Discussions", back_populates="comments")
    user = relationship("Users", back_populates="comments")