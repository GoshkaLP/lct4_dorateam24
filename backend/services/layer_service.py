from backend.utils.wrappers import db_error
from asyncpg import Connection


class LayerService:
    @db_error
    async def get_districts(self, db: Connection):
        response = await db.fetch("SELECT * FROM districts")
        return [{"id": row["id"], "title": row["district"]} for row in response]

    @db_error
    async def get_areas(self, db: Connection):
        response = await db.fetch("SELECT * FROM areas")
        return [{"id": row["id"], "title": row["area"]} for row in response]

    @db_error
    async def get_cadastrals(self, db: Connection):
        response = await db.fetch("SELECT * FROM cadastrals")
        return [{"id": row["id"], "title": row["cadastral"]} for row in response]

    @db_error
    async def get_addresses(self, db: Connection):
        response = await db.fetch("SELECT * FROM addresses")
        return [{"id": row["id"], "title": row["address"]} for row in response]
