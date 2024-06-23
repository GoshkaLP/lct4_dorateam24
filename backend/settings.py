from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


def get_model_config(env_prefix: str = "") -> SettingsConfigDict:
    return SettingsConfigDict(env_prefix=env_prefix, env_file=".env", extra="ignore")


class AppSettings(BaseSettings):
    name: str = "LCT dorateam 2024"
    version: str = "1.0.0"
    title: str = "LCT dorateam 2024"
    summary: str = "Проект 4 трека ЛЦТ 2024 команды dorateam"


class DBSettings(BaseSettings):
    hostname: str
    port: int
    password: str
    user: str
    db: str

    model_config = get_model_config(env_prefix="postgres_")

    @property
    def postgres_dsn(self):
        return f"postgresql://{self.user}:{self.password}@{self.hostname}:{self.port}/{self.db}"


class JWTSettings(BaseSettings):
    secret_key: str
    algorithm: str = "HS256"

    model_config = get_model_config()


app_settings = AppSettings()
db_settings = DBSettings()
jwt_settings = JWTSettings()
