from ..database import database
from sqlalchemy import CheckConstraint


class Address(database.Model):
    address_id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey("users.user_id"), nullable=False)
    address_line1 = database.Column(database.String(255), nullable=False)
    city = database.Column(database.String(255), nullable=False)
    state = database.Column(database.String(255), nullable=False)
    country = database.Column(database.String(255), nullable=False)
    postal_code = database.Column(database.String(255), nullable=False)
    is_default = database.Column(database.Boolean, default=True)
    address_type = database.Column(database.String(255), default="SHIPPING", nullable=False)

    __table_args__ = (CheckConstraint("address_type IN ('SHIPPING', 'BILLING')", name="ck_address_type"),)
