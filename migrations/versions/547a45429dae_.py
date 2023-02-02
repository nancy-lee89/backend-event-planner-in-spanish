"""empty message

Revision ID: 547a45429dae
Revises: 60d83e876445
Create Date: 2023-02-01 13:14:35.524917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '547a45429dae'
down_revision = '60d83e876445'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event_info', 'event_name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event_info', 'event_name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###