import bcrypt
from ..model.user import User
from ..database import database
from ..model.user_auth import UserAuth


class UserService:
    """A user service class."""

    @classmethod
    def get_user_by_id(cls, id: int):
        """A function to get user by ID."""

        user: User = User.query.get(id)

        return user

    @classmethod
    def get_users(cls):
        """A function to get a list of user."""

        users: list[User] = User.query.all()

        return users

    @classmethod
    def create_user(cls, user_detail: dict):
        """A function to create a user."""

        password = user_detail["password"].encode("utf-8")
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")

        user = User(
            first_name=user_detail["first_name"],
            last_name=user_detail["last_name"],
            email=user_detail["email"],
        )

        database.session.add(user)
        database.session.commit()

        user_auth = UserAuth(
            user_id=user.user_id,
            email=user.email,
            hashed_password=hashed_password,
            role="USER",
            status="ACTIVE",
        )

        database.session.add(user_auth)

        database.session.commit()

        return user

    @classmethod
    def delete_user_by_id(cls, id: int):
        """A function to delete user by ID."""

        user: User = User.query.get(id)
        if user is None:
            return None

        user_auth: UserAuth = UserAuth.query.filter_by(user_id=id).first()
        if user_auth:
            user_auth.status = "INACTIVE"
            database.session.commit()
        return user

    @classmethod
    def verify_user_password(cls, user_id: int, password: str):
        user_auth: UserAuth = UserAuth.query.filter_by(user_id=user_id).first()
        if user_auth is None:
            return False

        if bcrypt.checkpw(password.encode("utf-8"), user_auth.hashed_password):
            return True
        else:
            return False
