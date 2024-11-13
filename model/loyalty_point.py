from ..database import database


class LoyaltyPoints(database.Model):
    points_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(database.Integer, database.ForeignKey("users.user_id"), nullable=False)
    points = database.Column(database.Integer, nullable=False)
    created_at = database.Column(database.TIMESTAMP)
    reason = database.Column(database.String(255), nullable=False)
    status = database.Column(database.Enum("Gain", "Loss"))
