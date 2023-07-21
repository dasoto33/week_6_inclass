"""update

Revision ID: 2313f8833cea
Revises: 62b2cc6274a8
Create Date: 2023-07-18 14:39:40.789286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2313f8833cea'
down_revision = '62b2cc6274a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
