from ..database import database


class User(database.Model):
    user_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    first_name = database.Column(database.String(255), nullable=False)
    last_name = database.Column(database.String(255), nullable=False)
    dob = database.Column(database.Date)
    gender = database.Column(database.String(50))
    address = database.Column(database.String(255))
    phone_number = database.Column(database.String(15))
    email = database.Column(database.String(255), nullable=False, unique=True)
    profile_picture = database.Column(database.String(500))
    preferences = database.Column(database.JSON)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
