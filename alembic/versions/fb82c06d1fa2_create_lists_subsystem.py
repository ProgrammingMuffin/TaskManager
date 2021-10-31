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
    op.create_table("lists",
        sa.Column("id", sa.BIGINT, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("recurring_deadline", sa.Time, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("modified_at", sa.DateTime, nullable=False)
    )

    op.create_table("tasks",
        sa.Column("id", sa.BIGINT, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("status", sa.String(64), nullable=False),
        sa.Column("description", sa.Text),
        sa.Column("list_id", sa.BIGINT, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("modified_at", sa.DateTime, nullable=False),
        sa.ForeignKeyConstraint(['list_id'], ['lists.id'])
    )

    op.create_table("list_properties",
        sa.Column("id", sa.BIGINT, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("value", sa.Text, nullable=False),
        sa.Column("list_id", sa.BIGINT, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("modified_at", sa.DateTime, nullable=False),
        sa.ForeignKeyConstraint(['list_id'], ['lists.id'])
    )


def downgrade():
    op.drop_table("list_properties")
    op.drop_table("tasks")
    op.drop_table("lists")

