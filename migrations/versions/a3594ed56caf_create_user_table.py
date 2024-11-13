"""Create user table.

Revision ID: a3594ed56caf
Revises: be98c9e88441
Create Date: 2024-10-04 10:26:15.511459

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a3594ed56caf"
down_revision = "be98c9e88441"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("user_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("dob", sa.Date(), nullable=False),
        sa.Column("gender", sa.String(length=50), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("phone_number", sa.String(length=15), nullable=True),
        sa.Column("role", sa.Enum("admin", "user", name="user_role_enum"), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("profile_picture", sa.LargeBinary(), nullable=True),
        sa.Column("status", sa.Enum("active", "inactive", "banned", name="user_status_enum"), nullable=False),
        sa.Column("preferences", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint("user_id"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    # ### end Alembic commands ###