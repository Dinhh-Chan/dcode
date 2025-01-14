from sqlalchemy import Integer, String, Enum , Table , Column , Text, ForeignKey 
from sqlalchemy import relationship 
from sqlalchemy import func 
from . emun import GenderEnum, RoleEnum 
from . import Base 
import datetime
from datetime import Date 
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index= True)
    ho_va_ten = Column(String(255),nullable= False)
    gioi_tinh = Column(Enum(GenderEnum),default=GenderEnum.other)
    ngay_sinh = Column(Date)
    tieu_su = Column(Text, nullable=True)
    username = Column(String(100), unique=True, nullable= False )
    password= Column(String(255), nullable= False)
    diem= Column(Integer, default= 0  )
    role= Column(Enum(RoleEnum), default=RoleEnum.user)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)