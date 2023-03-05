"""Soft delete orders

Revision ID: 6f397fa823b6
Revises: 8cf609263523
Create Date: 2023-03-05 22:32:33.434916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f397fa823b6'
down_revision = '8cf609263523'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "orders",
        sa.Column(
            "deleted_at",
            sa.DateTime(timezone=False),
            nullable=True,
            default=None,
            index=True
        )
    )


def downgrade() -> None:
    op.drop_column("orders", "deleted_at")
