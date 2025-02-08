from pydantic import BaseModel , Optional
from datetime import datetime 
from typing import Optional 

class OrganizationBase(BaseModel):
    ten_to_chuc : str 
    mo_ta : Optional[str] = None  
    ngay_tao: Optional[datetime] = datetime.utcnow()
class OrganizationCreate(OrganizationBase):
    pass 
class OrganizationUpdate(OrganizationBase):
    pass 
class OrganizationReponse(OrganizationBase):
    id : int 
    class Config :
        orm_mode= True 
    