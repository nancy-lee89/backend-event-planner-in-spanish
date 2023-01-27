"""empty message

Revision ID: e20908ddf044
Revises: 8a65187e9cf9
Create Date: 2023-01-27 12:58:31.852343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e20908ddf044'
down_revision = '8a65187e9cf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact_info', sa.Column('first_name', sa.String(), nullable=True))
    op.drop_column('contact_info', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact_info', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('contact_info', 'first_name')
    # ### end Alembic commands ###