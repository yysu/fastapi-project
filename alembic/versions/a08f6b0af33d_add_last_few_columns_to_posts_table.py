"""add last few columns to posts table

Revision ID: a08f6b0af33d
Revises: 5ec3c752f2f8
Create Date: 2022-04-16 17:52:27.294474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a08f6b0af33d'
down_revision = '5ec3c752f2f8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass