from pydantic import BaseModel, EmailStr
class UserBase(BaseModel):
    ho_va_ten: str 
    username: str 
    email : str 
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