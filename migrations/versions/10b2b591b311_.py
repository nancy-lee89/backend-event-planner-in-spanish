"""empty message

Revision ID: 10b2b591b311
Revises: 547a45429dae
Create Date: 2023-02-06 11:32:24.237831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10b2b591b311'
down_revision = '547a45429dae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event_info', 'event_latitude',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=18, scale=10),
               existing_nullable=True)
    op.alter_column('event_info', 'event_longitude',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=18, scale=10),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event_info', 'event_longitude',
               existing_type=sa.Numeric(precision=18, scale=10),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('event_info', 'event_latitude',
               existing_type=sa.Numeric(precision=18, scale=10),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
