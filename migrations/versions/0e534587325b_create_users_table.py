"""create users table

Revision ID: 0e534587325b
Revises: c0dc668b67df
Create Date: 2025-09-26 02:44:17.133810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e534587325b'
down_revision: Union[str, Sequence[str], None] = 'c0dc668b67df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
