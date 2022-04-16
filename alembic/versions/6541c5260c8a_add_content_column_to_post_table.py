"""add content column to post table

Revision ID: 6541c5260c8a
Revises: 01005755f057
Create Date: 2022-04-16 17:36:49.327858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6541c5260c8a'
down_revision = '01005755f057'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade():
    op.drop_table('users')
