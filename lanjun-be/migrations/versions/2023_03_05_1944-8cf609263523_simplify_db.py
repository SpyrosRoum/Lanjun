"""Simplify db

Revision ID: 8cf609263523
Revises: 5adca8522a1a
Create Date: 2023-03-05 19:44:29.991616

"""
from uuid import uuid4

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '8cf609263523'
down_revision = '5adca8522a1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("reservation_tables")
    op.drop_table("reservations")
    op.drop_table("tables")

    op.drop_column("orders", "prepaid")



def downgrade() -> None:
    op.create_table(
        "tables",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("location", sa.Text, nullable=False),
        sa.Column("capacity", sa.Integer, nullable=False),
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
