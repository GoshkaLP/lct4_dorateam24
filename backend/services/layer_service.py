from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.models import Territories, Districts, Cadastrals, Areas, Addresses


class LayerService:
    async def get_districts(self, db: AsyncSession):
        response = await db.execute(select(Districts))
        records = response.scalars().all()
        return [{"id": row.id, "title": row.district} for row in records]

    async def get_areas(self, db: AsyncSession):
        response = await db.execute(select(Areas))
        records = response.scalars().all()
        return [{"id": row.id, "title": row.area} for row in records]

    async def get_cadastral(self, db: AsyncSession):
        response = await db.execute(select(Cadastrals))
        records = response.scalars().all()
        return [{"id": row.id, "title": row.cadastral} for row in records]

    async def get_addresses(self, db: AsyncSession):
        response = await db.execute(select(Addresses))
        records = response.scalars().all()
        return [{"id": row.id, "title": row.address} for row in records]
