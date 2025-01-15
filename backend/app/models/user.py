from sqlalchemy import Integer, String, Enum , Table , Column , Text, ForeignKey , Date, DateTime
from sqlalchemy.orm import relationship 
from sqlalchemy import func 
from . emun import GenderEnum, RoleEnum 
from . import Base 
import datetime
class users(Base):
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
    
    
    organization = relationship("Organizations", back_populates="users")
    submissions = relationship("Submissions", back_populates="user")
    user_courses = relationship("UserCourses", back_populates="user")
    contest_participants = relationship("ContestParticipants", back_populates="user")
    discussions = relationship("Discussions", back_populates="user")
    comments = relationship("Comments", back_populates="user")
    created_problems = relationship("Problems", back_populates="creator")
    created_courses = relationship("Courses", back_populates="creator")
    created_contests = relationship("Contests", back_populates="creator")