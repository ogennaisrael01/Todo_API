"""create users table

Revision ID: 688eae4beacc
Revises: d49ff2dca168
Create Date: 2025-09-26 02:23:27.962881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '688eae4beacc'
down_revision: Union[str, Sequence[str], None] = 'd49ff2dca168'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
