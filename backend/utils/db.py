import asyncpg
from backend.settings import db_settings


async def get_db() -> asyncpg.Connection:
    db = await asyncpg.connect(db_settings.postgres_dsn)
    try:
        yield db
    finally:
        await db.close()
