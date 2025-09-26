"""create users table

Revision ID: c0dc668b67df
Revises: 688eae4beacc
Create Date: 2025-09-26 02:27:58.668443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0dc668b67df'
down_revision: Union[str, Sequence[str], None] = '688eae4beacc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
