"""Init db

Revision ID: 57023cf01b4a
Revises:
Create Date: 2023-02-13 23:34:06.172972

"""
from uuid import uuid4

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "57023cf01b4a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "tables",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("location", sa.Text, nullable=False),
        sa.Column("capacity", sa.Integer, nullable=False),
    )

    op.create_table(
        "items",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("name", sa.Text, nullable=False, unique=True),
        sa.Column("description", sa.Text, nullable=False),
        sa.Column("price", sa.DECIMAL, nullable=False),
        sa.Column("count", sa.Integer, nullable=False),
        sa.Column("category", sa.Text, nullable=False),
        sa.Column("image_url", sa.Text, nullable=False),
    )

    op.create_table(
        "users",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("email", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("address", sa.Text, nullable=True),
        sa.Column("floor", sa.Text, nullable=True),
        sa.Column("bell", sa.Text, nullable=True),
        sa.Column("phone", sa.Text, nullable=False, unique=True),
        sa.Column("password", sa.Text, nullable=False),
        sa.Column("type", sa.Text),  # Admin or Normal
    )

    op.create_table(
        "orders",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("user_id", UUID(as_uuid=True), nullable=False, index=True),
        sa.Column("cost", sa.DECIMAL, nullable=False),
        sa.Column("prepaid", sa.Boolean, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=False), nullable=False),
        sa.ForeignKeyConstraint(("user_id",), ("users.id",)),
    )

    op.create_table(
        "reservations",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("user_id", UUID(as_uuid=True), nullable=False, index=True),
        sa.Column("starting_at", sa.DateTime(timezone=False), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=False), nullable=True),
        sa.Column("order_id", UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(("user_id",), ("users.id",)),
        sa.ForeignKeyConstraint(("order_id",), ("orders.id",)),
    )

    op.create_table(
        "reservation_tables",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("res_id", UUID(as_uuid=True), nullable=False),
        sa.Column("table_id", UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(("res_id",), ("reservations.id",)),
        sa.ForeignKeyConstraint(("table_id",), ("tables.id",)),
    )

    op.create_table(
        "order_items",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("order_id", UUID(as_uuid=True), nullable=False),
        sa.Column("item_id", UUID(as_uuid=True), nullable=False),
        sa.Column("item_count", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(("order_id",), ("orders.id",)),
        sa.ForeignKeyConstraint(("item_id",), ("items.id",)),
    )


def downgrade() -> None:
    op.drop_table("order_items")
    op.drop_table("reservation_tables")
    op.drop_table("reservations")
    op.drop_table("orders")
    op.drop_table("users")
    op.drop_table("items")
    op.drop_table("tables")
