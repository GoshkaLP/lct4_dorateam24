from backend.utils.wrappers import db_error
from backend.dto import PolygonsRequest
from asyncpg import Connection
import json


class AreasService:
    @db_error
    async def get_polygons(self, db: Connection, request_data: PolygonsRequest):
        conditions = []
        params = []
        count = 1
        if request_data.districts:
            conditions.append(f"t.district =  ANY(${count}::text[])")
            count += 1
            params.append(request_data.districts)
        if request_data.areas:
            conditions.append(f"t.area =  ANY(${count}::text[])")
            count += 1
            params.append(request_data.areas)
        if request_data.cadastrals:
            conditions.append(f"t.cadastral =  ANY(${count}::text[])")
            count += 1
            params.append(request_data.cadastrals)
        if request_data.addresses:
            conditions.append(f"t.address =  ANY(${count}::text[])")
            count += 1
            params.append(request_data.addresses)

        where_condition = " AND ".join(conditions) if conditions else "TRUE"
        stmt = f"""
            SELECT
                t.*,
                ST_AsGeoJSON(ST_Transform(t.geometry, 4326)) AS geojson
            FROM
                territories t
            WHERE {where_condition}
        """
        response = await db.fetch(stmt, *params)

        data = []
        for row in response:
            data.append(
                {
                    "properties": {
                        "id": row["id"],
                        "district": row["district"],
                        "area": row["area"],
                        "cadastral": row["cadastral"],
                        "address": row["address"],
                        "square": row["square"],
                        "isZpo": bool(row["is_zpo"]),
                        "isMsk": bool(row["is_msk"]),
                        "cntZouit": row["cnt_zouit"],
                        "shareZouit": row["share_zouit"],
                        "cntSprit": row["cnt_sprit"],
                        "share_sprit": row["share_sprit"],
                        "cntOozt": row["cnt_oozt"],
                        "shareOozt": row["share_oozt"],
                        "cntRent": row["cnt_rent"],
                        "shareRent": row["share_rent"],
                        "cntMkd": row["cnt_mkd"],
                        "shareMkd": row["share_mkd"],
                        "cntKrt": row["cnt_krt"],
                        "shareKrt": row["share_krt"],
                    },
                    "geometry": json.loads(row["geojson"]),
                }
            )
        return data
