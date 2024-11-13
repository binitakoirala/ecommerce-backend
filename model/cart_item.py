from ..database import database


class CartItems(database.Model):
    cart_item_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    cart_id = database.Column(database.Integer, database.ForeignKey("carts.cart_id"), nullable=False)
    product_id = database.Column(database.Integer, database.ForeignKey("product.id"), nullable=False)
    quantity = database.Column(database.Integer, nullable=False, default=1)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
