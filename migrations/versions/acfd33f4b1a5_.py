"""empty message

Revision ID: acfd33f4b1a5
Revises: 5bc3f5fbeba7
Create Date: 2019-03-09 18:34:05.973021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acfd33f4b1a5'
down_revision = '5bc3f5fbeba7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Authorization', 'created_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Authorization', sa.Column('created_at', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
