from ..database import database


class UserAuth(database.Model):
    auth_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey("user.user_id"), nullable=False)
    access_token = database.Column(database.String(255), nullable=False)
    refresh_token = database.Column(database.String(255), nullable=False)
    phone_number_verification = database.Column(database.String(15), nullable=False, unique=True)
    email_verification_token = database.Column(database.String(255), nullable=False, unique=True)
    hashed_password = database.Column(database.String(255), nullable=False)
    username = database.Column(database.String(50), nullable=False, unique=True)
    last_logged_in = database.Column(database.TIMESTAMP)
    email_verified = database.Column(database.Boolean, nullable=False)
    phone_number_verified = database.Column(database.Boolean, nullable=False)
    password_reset_token = database.Column(database.String(255), nullable=False, unique=True)
    locked_until = database.Column(database.TIMESTAMP)
    two_factor_enabled = database.Column(database.Boolean, nullable=True, default=False)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
