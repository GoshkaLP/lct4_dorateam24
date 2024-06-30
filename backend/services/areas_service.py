from backend.utils.wrappers import db_error
from backend.dto import PolygonsRequest
from backend.dependencies.colors import ColorsUtility
from asyncpg import Connection
from fastapi import HTTPException
import json


colors_utility = ColorsUtility()


class AreasService:
    def __init__(self):
        self.color_start = "#E10000"
        self.color_end = "#0DD344"

    def _add_color(self, objects: list[dict]):
        for i, obj in enumerate(objects):
            factor = i / (len(objects) - 1) if len(objects) > 1 else 0
            obj["properties"]["color"] = colors_utility.interpolate_color(
                self.color_start, self.color_end, factor
            )

    @db_error
    async def get_polygons(self, db: Connection, request_data: PolygonsRequest):
        conditions = []
        params = []
        count = 1
        if request_data.districts:
            conditions.append(f"t.district = ANY(${count}::text[])")
            count += 1
            params.append(request_data.districts)
        if request_data.areas:
            conditions.append(f"t.area = ANY(${count}::text[])")
            count += 1
            params.append(request_data.areas)
        if request_data.cadastrals:
            conditions.append(f"t.cadastral = ANY(${count}::text[])")
            count += 1
            params.append(request_data.cadastrals)
        if request_data.addresses:
            conditions.append(f"t.address = ANY(${count}::text[])")
            count += 1
            params.append(request_data.addresses)
        if request_data.crossingFilters:
            for key, val in request_data.crossingFilters.items():
                conditions.append(f"t.{key}::int {'>' if val == 0 else '>='} 0")
        if request_data.rectangleSearch:
            conditions.append(
                f"ST_Within(t.geometry, ST_MakeEnvelope(${count}, ${count+1}, ${count+2}, ${count+3}, 4326))"
            )
            count += 4
            params.extend(
                [
                    request_data.rectangleSearch.lonMin,
                    request_data.rectangleSearch.latMin,
                    request_data.rectangleSearch.lonMax,
                    request_data.rectangleSearch.latMax,
                ]
            )
        if request_data.radiusSearch:
            conditions.append(
                f"ST_DWithin(ST_Transform(t.geometry, 4326), ST_SetSRID(ST_MakePoint(${count}, ${count+1}), 4326), ${count+2})"
            )
            count += 3
            params.extend(
                [
                    request_data.radiusSearch.lon,
                    request_data.radiusSearch.lat,
                    request_data.radiusSearch.radius,
                ]
            )

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
            # determine weight
            if request_data.crossingFilters:
                weight = sum(
                    row[f"share_{key[key.find('_')+1:]}"] if "cnt" in key else 0
                    for key in request_data.crossingFilters.keys()
                )
                # print(f"Weight with certain share fields: {weight}")
            else:
                weight = sum(
                    [
                        row["share_zouit"],
                        row["share_sprit"],
                        row["share_oozt"],
                        row["share_rent"],
                        row["share_mkd"],
                        row["share_krt"],
                    ]
                )
                # print(f"Weight with all shares: {weight}")
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
                        "weight": weight,
                    },
                    "geometry": json.loads(row["geojson"]),
                }
            )
        data = sorted(data, key=lambda x: x["properties"]["weight"])
        self._add_color(data)
        return data

    @db_error
    async def get_search_history(self, db: Connection, user_id: int):
        stmt = "SELECT * FROM search_history WHERE user_id = $1"
        response = await db.fetch(stmt, user_id)
        if not response:
            raise HTTPException(
                detail=f"Search history not found for user {user_id}", status_code=404
            )
        return [
            {
                "id": row["id"],
                "user_id": row["user_id"],
                "search_request": row["search_request"],
                "date_created": row["date_created"],
            }
            for row in response
        ]
