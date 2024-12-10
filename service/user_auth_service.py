import bcrypt

from flask_jwt_extended import create_access_token, create_refresh_token
from ..model.user_auth import UserAuth
from ..database import database


class UserAuthService:
    """A user auth service class."""

    def login(self, email: str, password: str):
        user_auth: UserAuth = UserAuth.query.filter_by(email=email).first()

        if user_auth is None:
            return None

        if not bcrypt.checkpw(password.encode("utf-8"), user_auth.hashed_password.encode("utf-8")):
            return None

        access_token = create_access_token(identity={"email": email, "role": user_auth.role})
        refresh_token = create_refresh_token(identity={"email": email})

        return {"access_token": access_token, "refresh_token": refresh_token}
