from ..database import database


class Product(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(255), nullable=False)
    description = database.Column(database.String(255))
    price = database.Column(database.Float, nullable=False)
    stock_quantity = database.Column(database.Integer)
    brand = database.Column(database.String(255))
    weight = database.Column(database.String(255))
    dimension = database.Column(database.String(255))
    color = database.Column(database.String(255))
    size = database.Column(database.String(255))
    material = database.Column(database.String(255))
    discount = database.Column(database.Float)
    image_url = database.Column(database.String(255))
    is_active = database.Column(database.Boolean)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
