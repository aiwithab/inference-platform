from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Inference Platform"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
