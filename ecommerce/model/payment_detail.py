from ecommerce.main import database


class PaymentDetails(database.Model):
    payment_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    order_id = database.Column(database.Integer, database.ForeignKey("orders.order_id"), nullable=False)
    payment_date = database.Column(database.TIMESTAMP)
    payment_method = database.Column(
        database.Enum("CREDIT CARD", "DEBIT CARD", "PAYPAL", "NET BANKING", "CASH ON DELIVERY"), nullable=False
    )
    payment_status = database.Column(
        database.Enum("PENDING", "COMPLETED", "FAILED", "REFUNDED"), nullable=False, default="PENDING"
    )
    created_at = database.Column(database.TIMESTAMP)
