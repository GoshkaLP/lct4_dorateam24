from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from typing import Annotated
import jwt
from jwt import PyJWTError
from asyncpg import Connection
from backend.settings import jwt_settings
from backend.dto import TokenData, AuthForm
from backend.utils.wrappers import db_error

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()


class TokenUtility:
    def verify_password(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    def hash_password(self, plain_password: str):
        return pwd_context.hash(plain_password)

    @db_error
    async def auth_user(self, db: Connection, auth_form: AuthForm):
        response = await db.fetchrow(
            "SELECT * FROM users WHERE email = $1", auth_form.email
        )
        if response and self.verify_password(
            plain_password=auth_form.password, hashed_password=response["password"]
        ):
            payload = {"id": response["id"], "email": response["email"]}
            token = jwt.encode(
                payload, jwt_settings.secret_key, algorithm=jwt_settings.algorithm
            )
            return token
        raise HTTPException(detail="Wrong username or password", status_code=401)

    def __call__(
        self, credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
    ) -> TokenData:
        token = credentials.credentials
        try:
            payload = jwt.decode(
                token, jwt_settings.secret_key, algorithms=[jwt_settings.algorithm]
            )
            return TokenData(id=payload["id"], email=payload["email"])
        except PyJWTError as e:
            raise HTTPException(detail="Unable to verify token", status_code=401)


token_utility = TokenUtility()
