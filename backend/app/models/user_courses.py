from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from . import Base

class UserCourses(Base):
    __tablename__ = "user_courses"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("user_id", "course_id"),
    )

    user = relationship("Users", back_populates="user_courses")
    course = relationship("Courses", back_populates="user_courses")