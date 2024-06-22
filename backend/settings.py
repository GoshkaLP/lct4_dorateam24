from pydantic_settings import BaseSettings, SettingsConfigDict


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

    model_config = SettingsConfigDict(env_prefix="postgres_", env_file=".env")

    @property
    def postgres_dsn(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.hostname}:{self.port}/{self.db}"


app_settings = AppSettings()
db_settings = DBSettings()
