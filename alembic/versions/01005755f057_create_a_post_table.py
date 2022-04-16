"""create a post table

Revision ID: 01005755f057
Revises: 82cf9074e464
Create Date: 2022-04-16 17:17:43.402818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01005755f057'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))


def downgrade():
    pass
