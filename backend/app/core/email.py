import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from typing import List 
import random 
import string 
SMTP_SEVER = "smtp.gmail.com"
SMPT_PORT  = 587 
SENDER_EMAIL = "dinhtran29092005@gmail.com"
SENDER_PASSWORD ="kgow obrd xtwn mgnp"

def send_email_code(reciptien_email: str, code: str):
    """Mã xác thực đến người dùng """
    subject = "Xác thực đăng ký"
    body = f"Xin chào, chúng tôi nhận được yêu cầu đăng ký từ bạn, nếu người đăng ký không phải là bạn, hãy bỏ qua email này
    Mã xác thực của bạn là: {code} 
    "
    msg = MIMEMultipart()
    msg["From"]= SENDER_EMAIL 
    msg["To"]= reciptien_email
    msg["Subject"]= subject 
    msg.attach(MIMEText(body, "plain"))
    try :
        sever = smtplib.SMTP(SMTP_SEVER, SMPT_PORT)
        sever.starttls()
        sever.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        sever.sendmail(SENDER_EMAIL, reciptien_email, text)
        sever.quit()
    except Exception as e :
        print(f"Cannot send email")
def generate_code(length=6) -> str :
    charecters = string.ascii_letters + string.digits 
    return ''.join(random.choice(charecters) for i in range(length))