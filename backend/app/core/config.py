import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import List

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
load_dotenv(os.path.join(BASE_DIR, '.env'))  # Nạp biến môi trường từ file .env

class Settings(BaseSettings):
    PROJECT_NAME: str = 'FASTAPI_BASE'  # Giá trị mặc định nếu không có trong .env
    SECRET_KEY: str = ''  # Giá trị mặc định nếu không có trong .env
    API_PREFIX: str = ''
    BACKEND_CORS_ORIGINS: List[str] = ['*']
    DATABASE_URL: str = 'postgresql+psycopg2://root:password@localhost:5438/data_code'  # Giá trị mặc định
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECURITY_ALGORITHM: str = 'HS256'
    LOGGING_CONFIG_FILE: str = os.path.join(BASE_DIR, 'logging.ini')

    class Config:
        env_file = ".env"  # Đảm bảo rằng tệp .env được đọc từ thư mục hiện tại

settings = Settings()  # Tạo đối tượng settings và nạp các biến môi trường từ .env
