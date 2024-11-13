from ..model.user import User


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
