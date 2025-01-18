from ..database import database


class ShippingDetails(database.Model):
    shipping_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    order_id = database.Column(database.Integer, database.ForeignKey("orders.order_id"), nullable=False)
    tracking_number = database.Column(database.String(255))
    shipping_date = database.Column(database.TIMESTAMP)
    estimated_delivery_date = database.Column(database.TIMESTAMP)
    status = database.Column(database.Enum("PENDING", "SHIPPED", "IN TRANSIT", "DELIVERED"), default="PENDING")
