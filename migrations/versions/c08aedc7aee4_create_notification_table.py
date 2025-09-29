"""create notification table

Revision ID: c08aedc7aee4
Revises: 0e534587325b
Create Date: 2025-09-27 20:51:31.425070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c08aedc7aee4'
down_revision: Union[str, Sequence[str], None] = '0e534587325b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
