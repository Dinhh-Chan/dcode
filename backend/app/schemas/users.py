from pydantic import BaseModel, EmailStr
from typing import Optional 
from datetime import datetime 
from .. models.enums import GenderEnum, RoleEnum
class UserBase(BaseModel):
    ho_va_ten: str 
    username: str 
    email : str 
    gioi_tinh: Optional[GenderEnum] = GenderEnum.other 
    diem: Optional[int] = 0 
    role: Optional[RoleEnum]= RoleEnum.user
class UserLogin(BaseModel):
    username: str
    password: str 
class UserCreate(UserBase):
    password: str 
class UserOut(UserBase):
    id: int 
    class Config: 
        orm_mode = True 
class EmailVerification(BaseModel):
    email: EmailStr
    verification_code :str 
class UserLoginByEmail(BaseModel):
    email: str 
    verification_code : str 
class UserUpdate(UserBase):
    password: Optional[str] = None  
    ngay_sinh: Optional[datetime] = None 
    tieu_su: Optional[str]= None 