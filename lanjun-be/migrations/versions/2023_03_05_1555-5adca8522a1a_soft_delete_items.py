"""Soft delete items

Revision ID: 5adca8522a1a
Revises: 57023cf01b4a
Create Date: 2023-03-05 15:55:10.697487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5adca8522a1a'
down_revision = '57023cf01b4a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "items",
        sa.Column(
            "deleted_at",
            sa.DateTime(timezone=False),
            nullable=True,
            default=None,
            index=True
        )
    )


def downgrade() -> None:
    op.drop_column("items", "deleted_at")
