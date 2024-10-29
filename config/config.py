# app.py
from functools import lru_cache
from pydantic_settings import BaseSettings 
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 설정 클래스 정의
class Settings(BaseSettings):
    DB_TYPE: str
    DB_HOST: str
    DB_USER: str
    DB_PASSWD: str
    DB_PORT: int
    DB_NAME: str
    JWT_SECRET_KEY: str

    class Config:
        env_file = ".env"

# lru_cache를 사용하여 설정을 캐시
@lru_cache()
def get_settings():
    return Settings()
