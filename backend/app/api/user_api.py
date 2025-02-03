from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.schemas.users import UserLogin, UserOut, EmailVerification, UserCreate, UserLoginByEmail, UserUpdate 
from app.services.user_services import register_user_service, verify_email_service, login_user_service, send_verification_code_service, login_by_email_service, update_user, delete_user

router = APIRouter()

# Đăng ký người dùng
@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    result = register_user_service(user, db)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    return {"message": "Đăng ký thành công, hãy kiểm tra mã xác thực trong hòm thư email của bạn"}

# Xác thực email
@router.post("/verify-email")
def verify_email(verification: EmailVerification, db: Session = Depends(get_db)):
    result = verify_email_service(verification, db)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    return {"message": "Xác thực thành công"}

# Đăng nhập người dùng bằng username
@router.post("/login-by-username")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    result = login_user_service(user, db)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    return result

# Gửi lại mã xác thực qua email
@router.post("/send-verification-code")
def send_verification_code(verification: EmailVerification, db: Session = Depends(get_db)):
    result = send_verification_code_service(verification, db)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    return {"message": "Mã xác thực đã được gửi lại qua email"}

# Đăng nhập người dùng bằng email và mã xác thực
@router.post("/login-by-email")
def login_by_email(user: UserLoginByEmail, db: Session = Depends(get_db)):
    result = login_by_email_service(user, db)
    if "error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    return {"message": "Đăng nhập thành công"}


@router.put("/update/{username}", response_model= UserOut)
def update_user(username: str, user: UserUpdate, db: Session= Depends(get_db)):
    user_update = update_user(user, db, username)
    if "error" in user_update:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=user_update["error"])
    return user_update 
@router.delete("/delete/{username}", response_model= UserOut) 
def delete_user(username: str, db: Session= Depends(get_db)):
    res = delete_user(db, username)
    if "error" in res :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=res["error"])
    return res