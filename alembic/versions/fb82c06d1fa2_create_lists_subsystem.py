"""create lists subsystem

Revision ID: fb82c06d1fa2
Revises: 
Create Date: 2021-10-09 08:37:34.878611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb82c06d1fa2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("lists")
    op.add_column("lists", sa.Column("name", sa.Text))
    op.add_column("lists", sa.Column("recurring_deadline", sa.Time)
    op.add_column("lists", sa.Column("created_at", sa.DateTime))
    op.add_column("lists", sa.Column("modified_at", sa.DateTime))


def downgrade():
    op.drop_table("lists")

