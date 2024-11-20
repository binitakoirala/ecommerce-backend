from datetime import datetime, timezone
from ..database import database


class UserAuth(database.Model):
    auth_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey("user.user_id"), nullable=False)
    access_token = database.Column(database.String(255))
    refresh_token = database.Column(database.String(255))
    phone_verification_token = database.Column(database.String(15))
    email_verification_token = database.Column(database.String(255))
    hashed_password = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(50), nullable=False, unique=True)
    role = database.Column(database.Enum("ADMIN", "USER", name="user_role_enum"), nullable=False)
    last_logged_in = database.Column(database.TIMESTAMP)
    email_verified = database.Column(database.Boolean, nullable=False, default=False)
    phone_number_verified = database.Column(database.Boolean, nullable=False, default=False)
    password_reset_token = database.Column(database.String(255), nullable=True)
    locked_until = database.Column(database.TIMESTAMP)
    two_factor_enabled = database.Column(database.Boolean, nullable=True, default=False)
    created_at = database.Column(database.TIMESTAMP, default=datetime.now(tz=timezone.utc))
    updated_at = database.Column(database.TIMESTAMP, default=datetime.now(tz=timezone.utc))
