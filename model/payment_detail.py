from main import database


class PaymentDetails(database.Model):
    payment_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    order_id = database.Column(database.Integer, database.ForeignKey("orders.order_id"), nullable=False)
    payment_date = database.Column(database.TIMESTAMP)
    payment_method = database.Column(
        database.Enum("Credit Card", "Debit Card", "Paypal", "Net Banking", "Cash On Delivery"), nullable=False
    )
    payment_status = database.Column(
        database.Enum("Pending", "Completed", "Failed", "Refunded"), nullable=False, default="Pending"
    )
    created_at = database.Column(database.TIMESTAMP)
