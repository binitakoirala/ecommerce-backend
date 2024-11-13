from ..database import database


class OrderItems(database.Model):
    order_item_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    order_id = database.Column(database.Integer, database.ForeignKey("orders.order_id"), nullable=False)
    product_name = database.Column(database.String(255), nullable=False)
    quantity = database.Column(database.Integer, nullable=False, default=1)
    price = database.Column(database.Float, nullable=False)
    description = database.Column(database.Text)
    discount_amount = database.Column(database.Float)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
