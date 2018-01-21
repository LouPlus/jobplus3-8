"""empty message

Revision ID: aa08f6f52439
Revises: 7dcc7315f2b0
Create Date: 2018-01-21 21:25:45.712616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa08f6f52439'
down_revision = '7dcc7315f2b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'company', 'user', ['user_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'company', type_='foreignkey')
    op.drop_column('company', 'user_id')
    # ### end Alembic commands ###
