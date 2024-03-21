"""create events tables

Revision ID: 7166f9fa4321
Revises: 
Create Date: 2024-03-13 02:05:33.451183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = '7166f9fa4321'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\"")
    op.create_table(
        'event',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_by_user_id', sa.Integer(),
                  nullable=False, index=True),
        sa.Column('title', sa.String(length=30), nullable=False),
        sa.Column('about', sa.String(length=63206), nullable=False),
        sa.Column('location', sa.String(length=100), nullable=True),
        sa.Column('start_time', sa.DateTime(timezone=True), nullable=False),
        sa.Column('end_time', sa.DateTime(timezone=True), nullable=False),
        sa.Column('agenda', sa.JSON(), nullable=True),
        sa.Column('faqs', sa.JSON(), nullable=True),
        sa.Column('uuid', UUID(as_uuid=True), nullable=False,
                  server_default=sa.text("uuid_generate_v4()::UUID")),
        sa.Column('media_url', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('is_deleted', sa.Boolean(),
                  nullable=False, server_default='0'),
        sa.PrimaryKeyConstraint('id', 'uuid'),
        sa.UniqueConstraint('uuid')
    )


def downgrade() -> None:
    op.drop_table('event')
