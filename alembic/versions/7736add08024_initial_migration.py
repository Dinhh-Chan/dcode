"""Initial migration

Revision ID: 7736add08024
Revises: ca885dfa5bf4
Create Date: 2025-01-17 11:06:56.962801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7736add08024'
down_revision: Union[str, None] = 'ca885dfa5bf4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.add_column('users', sa.Column('email_verified', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('verification_code', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'verification_code')
    op.drop_column('users', 'email_verified')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###