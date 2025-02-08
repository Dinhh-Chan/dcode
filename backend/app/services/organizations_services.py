from fastapi import HTTPException, status 
from app.schemas.organizations_sche import OrganizationBase , OrganizationCreate, OrganizationReponse, OrganizationUpdate
from sqlalchemy.orm import Session 
from app.models.organizations import Organizations 


#add organization 
