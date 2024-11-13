from ..database import database


class User(database.Model):
    user_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    first_name = database.Column(database.String(255), nullable=False)
    last_name = database.Column(database.String(255), nullable=False)
    dob = database.Column(database.Date, nullable=False)
    gender = database.Column(database.String(50))
    address = database.Column(database.String(255))
    phone_number = database.Column(database.String(15))
    role = database.Column(database.Enum("admin", "user", name="user_role_enum"), nullable=False)
    email = database.Column(database.String(255), nullable=False, unique=True)
    profile_picture = database.Column(database.LargeBinary)  # String(500)
    status = database.Column(database.Enum("active", "inactive", "banned", name="user_status_enum"), nullable=False)
    preferences = database.Column(database.JSON)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
