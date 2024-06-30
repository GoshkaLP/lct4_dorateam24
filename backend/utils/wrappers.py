from functools import wraps
from fastapi import HTTPException
from asyncpg.exceptions import PostgresError


def db_error(func):
    @wraps(func)
    async def wrapped(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ConnectionError as e:
            raise HTTPException(
                detail=f"DB connection error: {str(e)}", status_code=500
            )
        except PostgresError as ee:
            raise HTTPException(detail=f"DB service error: {str(ee)}", status_code=500)

    return wrapped
