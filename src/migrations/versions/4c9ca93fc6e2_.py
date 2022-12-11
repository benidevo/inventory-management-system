"""empty message

Revision ID: 4c9ca93fc6e2
Revises: ca4ae6739cdb
Create Date: 2022-12-10 21:18:16.048270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4c9ca93fc6e2"
down_revision = "ca4ae6739cdb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("cart", schema=None) as batch_op:
        batch_op.drop_column("quantity")
        batch_op.drop_column("total_amount")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("cart", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("total_amount", sa.INTEGER(), autoincrement=False, nullable=False)
        )
        batch_op.add_column(
            sa.Column("quantity", sa.INTEGER(), autoincrement=False, nullable=False)
        )

    # ### end Alembic commands ###