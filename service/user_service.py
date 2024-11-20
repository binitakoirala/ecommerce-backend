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

        user = User(
            first_name=user_detail["first_name"],
            last_name=user_detail["last_name"],
            email=user_detail["email"],
            status="active"
        )

        database.session.add(user)
        database.session.commit()

        user_auth = UserAuth(
            user_id=user.user_id,
            email=user.email,
            hashed_password=user_detail["password"],
            role="USER"
        )

        database.session.add(user_auth)

        database.session.commit()

        return user