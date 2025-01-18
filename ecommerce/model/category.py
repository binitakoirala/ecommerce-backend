from ..database import database


class Category(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(255), nullable=False)
    description = database.Column(database.String(255))
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
