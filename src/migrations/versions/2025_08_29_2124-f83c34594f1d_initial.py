"""initial

Revision ID: f83c34594f1d
Revises:
Create Date: 2025-08-29 21:24:58.859334

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "f83c34594f1d"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
