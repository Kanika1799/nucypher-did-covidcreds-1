"""Add Name

Revision ID: a775bd26132e
Revises: 5f306060b731
Create Date: 2020-07-07 02:08:00.874532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a775bd26132e'
down_revision = '5f306060b731'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('did', sa.Column('name', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('did', 'name')
    # ### end Alembic commands ###
