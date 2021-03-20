"""empty message

Revision ID: e188a4d79a9e
Revises: 
Create Date: 2021-03-20 14:33:47.080975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e188a4d79a9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('bedrooms', sa.INTEGER(), nullable=True),
    sa.Column('bathrooms', sa.INTEGER(), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('price', sa.String(length=80), nullable=True),
    sa.Column('proptype', sa.String(length=80), nullable=True),
    sa.Column('pic_name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
