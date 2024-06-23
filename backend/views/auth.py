from fastapi import APIRouter, Depends
from asyncpg import Connection
from backend.dto import AuthForm, Token, TokenData
from backend.dependencies.token import token_utility
from backend.utils.db import get_db

router = APIRouter(tags=["Auth"], prefix="/user")


@router.post("/auth")
async def auth_user(auth_form: AuthForm, db: Connection = Depends(get_db)):
    token = await token_utility.auth_user(db=db, auth_form=auth_form)
    return Token.model_validate({"token": token})


@router.get("/token", response_model=TokenData)
def token_data(token_data: TokenData = Depends(token_utility)):
    return token_data
