from ..database import database


class Orders(database.Model):
    order_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey("users.user_id"), nullable=False)
    full_name = database.Column(database.String(255))
    phone_number = database.Column(database.String(15))
    email = database.Column(database.String(255))
    order_date = database.Column(database.TIMESTAMP)
    status = database.Column(
        database.Enum("pending", "processing", "shipped", "delivered", "cancelled"), default="pending"
    )
    total_amount = database.Column(database.Float)
    shipping_address = database.Column(database.String(255), nullable=False)
    billing_address = database.Column(database.String(255), nullable=False)
