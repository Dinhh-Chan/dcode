import logging
import uvicorn
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Base
from app.core.config import settings
from app.helpers.exception_handler import CustomException, http_exception_handler
from .database import SessionLocal  # Sử dụng SessionLocal từ cơ sở dữ liệu của bạn.

logging.config.fileConfig(settings.LOGGING_CONFIG_FILE, disable_existing_loggers=False)

engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url="/docs", 
        redoc_url='/re-docs',
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        description='''
        Base frame with FastAPI micro framework + Postgresql
            - Login/Register with JWT
            - Permission
            - CRUD User
            - Unit testing with Pytest
            - Dockerize
        '''
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_exception_handler(CustomException, http_exception_handler)

    return application

# Session creator for database interaction
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Tạo và chạy ứng dụng
app = get_application()

# Đảm bảo rằng các bảng được tạo ra khi ứng dụng khởi động
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
