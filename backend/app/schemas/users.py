from pydantic import BaseModel, EmailStr
from typing import Optional
from .. models.enums import GenderEnum, RoleEnum
from datetime import datetime

# Base schema cho người dùng, dùng chung cho các schema khác
class UserBase(BaseModel):
    ho_va_ten: str
    gioi_tinh: Optional[GenderEnum] = GenderEnum.other
    email: EmailStr
    username: str
    diem: Optional[int] = 0
    role: Optional[RoleEnum] = RoleEnum.user

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    ho_va_ten: Optional[str] = None
    gioi_tinh: Optional[GenderEnum] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    tieu_su: Optional[str] = None
    ngay_sinh: Optional[datetime] = None
    diem: Optional[int] = None
    role: Optional[RoleEnum] = None

    class Config:
        orm_mode = True

class UserOut(UserBase):
    id: int
    ngay_sinh: Optional[datetime]
    tieu_su: Optional[str]

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class UserLoginByEmail(BaseModel):
    email: EmailStr
    verification_code: str

class EmailVerification(BaseModel):
    email: EmailStr
    verification_code: str

    class Config:
        orm_mode = True
