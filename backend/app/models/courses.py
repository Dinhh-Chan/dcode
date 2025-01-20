from sqlalchemy import Integer, String , Column , ForeignKey ,DateTime
from . import Base 
import datetime 
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship  
class Courses(Base):
    __tablename__ = "courses"
    id = Column(Integer,primary_key= True, index=True)
    ten_khoa_hoc = Column(String(255), nullable= False)
    mo_ta = Column(String)
    ngay_tao = Column(DateTime, server_default= func.now())
    nguoi_tao_id = Column(Integer, ForeignKey("users.id"))
    
    creator = relationship("Users", back_populates="created_courses")
    course_problems = relationship("CourseProblems", back_populates="course")
    user_courses = relationship("UserCourses", back_populates="course")