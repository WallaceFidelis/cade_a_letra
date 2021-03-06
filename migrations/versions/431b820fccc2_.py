"""empty message

Revision ID: 431b820fccc2
Revises: 49d8078b08a4
Create Date: 2019-03-09 18:26:53.701882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '431b820fccc2'
down_revision = '49d8078b08a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Authorization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_token', sa.String(), nullable=False),
    sa.Column('token_type', sa.String(), nullable=False),
    sa.Column('expires_in', sa.Integer(), nullable=False),
    sa.Column('refresh_token', sa.String(), nullable=False),
    sa.Column('scope', sa.String(), nullable=False),
    sa.Column('created_at', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('authorization')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authorization',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('access_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('token_type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('expires_in', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('refresh_token', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('scope', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='authorization_pkey')
    )
    op.drop_table('Authorization')
    # ### end Alembic commands ###
