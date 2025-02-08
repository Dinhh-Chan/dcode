from passlib.context import CryptContext 
from datetime import datetime, timedelta 
import jwt 
from typing import Optional 
from fastapi import HTTPException, status 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

def get_password_hash(password: str) -> str :
    return pwd_context.hash(password)
def verify_password(plain_password: str , hased_password: str)-> bool:
    return pwd_context.verify(plain_password, hased_password)

SECRET_KEY ="thangdatngunhucho"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPRIRE_MINUTES= 30 

def create_access_token(data: dict, expries_delta:Optional[timedelta]= None)-> str :
    to_endcode = data.copy()
    if expries_delta :
        expire = datetime.utcnow()+ expries_delta
    else : 
        expire = datetime.utcnow() + timedelta(minutes= 60)
    to_endcode.update({"exp": expire})
    encode_jwt = jwt.encode(to_endcode, SECRET_KEY, algorithm= ALGORITHM)
    return encode_jwt

def verify_token(token: str)-> dict :
    try : 
        payload = jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Invalid token")