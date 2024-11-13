from ..database import database


class RatingsReviews(database.Model):
    review_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    order_id = database.Column(database.Integer, nullable=False)
    product_id = database.Column(database.Integer, database.ForeignKey("product.id"), nullable=False)
    user_id = database.Column(database.Integer, database.ForeignKey("users.user_id"), nullable=False)
    rating = database.Column(database.Integer, nullable=False)
    review_text = database.Column(database.Text)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
