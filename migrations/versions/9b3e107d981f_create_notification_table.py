"""create notification table

Revision ID: 9b3e107d981f
Revises: c08aedc7aee4
Create Date: 2025-09-27 20:52:29.425846

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b3e107d981f'
down_revision: Union[str, Sequence[str], None] = 'c08aedc7aee4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
