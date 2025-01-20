from datetime import datetime
from app.db.db import get_db
from sqlalchemy.orm import Session
from app.core.security import verify_password, create_access_token, get_password_hash
from app.core.email import send_email_code, generate_code
from app.schemas.users import UserLogin, UserOut, EmailVerification, UserCreate, UserBase, UserLoginByEmail
from fastapi import APIRouter, HTTPException, Depends, status
from app.models.user import Users

router = APIRouter()

# Đăng ký người dùng
@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    check_user_email = db.query(Users).filter(Users.email == user.email).first()
    check_username = db.query(Users).filter(Users.username == user.username).first()
    
    if check_user_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email này đã tồn tại, vui lòng nhập email khác.")
    
    if check_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tài khoản này đã tồn tại, vui lòng nhập tài khoản khác.")
    
    hash_password = get_password_hash(user.password)
    verification_code = generate_code()
    
    db_user = Users(
        ho_va_ten=user.ho_va_ten,
        username=user.username,
        password=hash_password,
        email=user.email,
        email_verified=None,
        verification_code=verification_code
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    send_email_code(user.email, verification_code)
    
    return {"message": "Đăng ký thành công, hãy kiểm tra mã xác thực trong hòm thư email của bạn"}

# Xác thực email
@router.post("/verify-email")
def verify_email(verification: EmailVerification, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.email == verification.email).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email không tồn tại")
    
    db_verification_code = db_user.verification_code

    if verification.verification_code == db_verification_code:
        db_user.email_verified = datetime.utcnow()  # Cập nhật thời gian xác thực
        db_user.verification_code = generate_code()  # Cập nhật mã xác thực mới
        db.commit()
        return {"message": "Xác thực thành công"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mã xác thực không hợp lệ")

# Đăng nhập người dùng bằng username
@router.post("/login-by-username")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.username == user.username).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tài khoản hoặc mật khẩu không đúng")
    
    # Kiểm tra mật khẩu
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tài khoản hoặc mật khẩu không đúng")
    
    # Kiểm tra trạng thái email
    if db_user.email_verified is None: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bạn cần xác thực email trước")
    
    # Tạo access token
    access_token = create_access_token(user_id=db_user.username)  # Truyền username làm user_id
    
    return {"message": "Đăng nhập thành công", "access_token": access_token}

# Gửi lại mã xác thực qua email
@router.post("/send-verification-code")
def send_verification_code(verification: EmailVerification, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.email == verification.email).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email không tồn tại")
    
    verification_code = generate_code()
    send_email_code(db_user.email, verification_code)
    db_user.verification_code = verification_code
    db.commit()
    
    return {"message": "Mã xác thực đã được gửi lại qua email"}

# Đăng nhập người dùng bằng email và mã xác thực
@router.post("/login-by-email")
def login_by_email(user: UserLoginByEmail, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Người dùng không tồn tại")
    
    # Kiểm tra mã xác thực
    if db_user.verification_code == user.verification_code:
        db_user.verification_code= generate_code()
        return {"message": "Đăng nhập thành công"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Mã xác thực không hợp lệ")
