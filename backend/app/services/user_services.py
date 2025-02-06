from sqlalchemy.orm import Session
from app.models.user import Users
from app.core.security import verify_password, create_access_token, get_password_hash
from app.core.email import send_email_code, generate_code
from app.schemas.users import UserUpdate, UserCreate, UserLogin, EmailVerification, UserLoginByEmail
from datetime import datetime
from sqlalchemy import desc
# Đăng ký người dùng
def register_user_service(user: UserCreate, db: Session):
    check_user_email = db.query(Users).filter(Users.email == user.email).first()
    check_username = db.query(Users).filter(Users.username == user.username).first()

    if check_user_email:
        return {"error": "Email này đã tồn tại, vui lòng nhập email khác."}
    if check_username:
        return {"error": "Tài khoản này đã tồn tại, vui lòng nhập tài khoản khác."}
    
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
def verify_email_service(verification: EmailVerification, db: Session):
    db_user = db.query(Users).filter(Users.email == verification.email).first()

    if not db_user:
        return {"error": "Email không tồn tại"}

    db_verification_code = db_user.verification_code

    if verification.verification_code == db_verification_code:
        db_user.email_verified = datetime.utcnow()  # Cập nhật thời gian xác thực
        db_user.verification_code = generate_code()  # Cập nhật mã xác thực mới
        db.commit()
        return {"message": "Xác thực thành công"}
    else:
        return {"error": "Mã xác thực không hợp lệ"}

# Đăng nhập người dùng bằng username
def login_user_service(user: UserLogin, db: Session):
    db_user = db.query(Users).filter(Users.username == user.username).first()

    if not db_user:
        return {"error": "Tài khoản hoặc mật khẩu không đúng"}
    
    # Kiểm tra mật khẩu
    if not verify_password(user.password, db_user.password):
        return {"error": "Tài khoản hoặc mật khẩu không đúng"}
    
    # Kiểm tra trạng thái email
    if db_user.email_verified is None: 
        return {"error": "Bạn cần xác thực email trước"}
    
    # Tạo access token
    access_token = create_access_token(user_id=db_user.username)  # Truyền username làm user_id
    
    return {"message": "Đăng nhập thành công", "access_token": access_token}

# Gửi lại mã xác thực qua email
def send_verification_code_service(verification: EmailVerification, db: Session):
    db_user = db.query(Users).filter(Users.email == verification.email).first()

    if not db_user:
        return {"error": "Email không tồn tại"}
    
    verification_code = generate_code()
    send_email_code(db_user.email, verification_code)
    db_user.verification_code = verification_code
    db.commit()
    
    return {"message": "Mã xác thực đã được gửi lại qua email"}

# Đăng nhập người dùng bằng email và mã xác thực
def login_by_email_service(user: UserLoginByEmail, db: Session):
    db_user = db.query(Users).filter(Users.email == user.email).first()

    if not db_user:
        return {"error": "Người dùng không tồn tại"}
    
    # Kiểm tra mã xác thực
    if db_user.verification_code == user.verification_code:
        access_token = create_access_token(user_id=db_user.username) 
        db_user.verification_code = generate_code()
        db.commit()
        return {"message": "Đăng nhập thành công", "access token": access_token}
    else:
        return {"error": "Mã xác thực không hợp lệ"}
# Chỉnh sửa thông tin người dùng 
def update_user(user: UserUpdate , db: Session, user_name : str): 
    db_user = db.query(Users).filter(Users.username == user_name).first()
    if not db_user:
        return {"error": "Người dùng không tồn tại"}

    if user.ho_va_ten:
        db_user.ho_va_ten = user.ho_va_ten
    if user.gioi_tinh:
        db_user.gioi_tinh = user.gioi_tinh
    if user.email:
        db_user.email = user.email
    if user.username:
        db_user.username = user.username
    if user.password:
        db_user.password = get_password_hash(user.password)
    if user.tieu_su:
        db_user.tieu_su = user.tieu_su
    if user.ngay_sinh:
        db_user.ngay_sinh = user.ngay_sinh
    if user.diem is not None:
        db_user.diem = user.diem
    if user.role:
        db_user.role = user.role
    
    db.commit()
    db.refresh(db_user)
    return db_user
# Delete user 
def delete_user(db: Session , user_name: str  ):
    db_user = db.query(Users).filter(Users.username == user_name)
    if not db_user:
        return {"error": "Người dùng không tồn tại"}

    db.delete(db_user)
    db.commit()
    return db_user

def get_user(db: Session , user_name: str ):
    db_user = db.query(Users).filter(Users.username == user_name).first()
    if not db_user :
        return None 
    return db_user 
def get_user_order_by_diem(db: Session):
    db_user = db.query(Users).order_by(desc(Users.diem)).all()
    if not db_user :
        return None 
    return db_user 