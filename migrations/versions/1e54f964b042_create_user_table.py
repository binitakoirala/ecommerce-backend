"""Create user table

Revision ID: 1e54f964b042
Revises: 237b67363223
Create Date: 2024-11-21 22:14:34.260614

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1e54f964b042"
down_revision = "237b67363223"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("user_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("dob", sa.Date(), nullable=True),
        sa.Column("gender", sa.String(length=50), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("phone_number", sa.String(length=15), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("profile_picture", sa.String(length=500), nullable=True),
        sa.Column("preferences", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint("user_id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "user_auth",
        sa.Column("auth_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("access_token", sa.String(length=255), nullable=True),
        sa.Column("refresh_token", sa.String(length=255), nullable=True),
        sa.Column("phone_verification_token", sa.String(length=15), nullable=True),
        sa.Column("email_verification_token", sa.String(length=255), nullable=True),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=50), nullable=False),
        sa.Column("role", sa.Enum("ADMIN", "USER", name="user_auth_role_enum"), nullable=False),
        sa.Column("status", sa.Enum("ACTIVE", "INACTIVE", "BANNED", name="user_auth_status_enum"), nullable=False),
        sa.Column("last_logged_in", sa.TIMESTAMP(), nullable=True),
        sa.Column("email_verified", sa.Boolean(), nullable=False),
        sa.Column("phone_number_verified", sa.Boolean(), nullable=False),
        sa.Column("password_reset_token", sa.String(length=255), nullable=True),
        sa.Column("locked_until", sa.TIMESTAMP(), nullable=True),
        sa.Column("two_factor_enabled", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.user_id"],
        ),
        sa.PrimaryKeyConstraint("auth_id"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_auth")
    op.drop_table("user")
    # ### end Alembic commands ###
