"""empty message

Revision ID: 0066575284ef
Revises: 
Create Date: 2024-07-15 19:12:21.488744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0066575284ef'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_api',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resumes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('workload', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users_api.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # op.drop_table('operation')
    # op.drop_table('user')
    # op.drop_table('resume')
    # op.drop_table('role')
    # op.drop_table('workers')
    # ### end Alembic commands ###


def downgrade() -> None:
    pass
    # # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('workers',
    # sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('workers_id_seq'::regclass)"), autoincrement=True, nullable=False),
    # sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('id', name='workers_pkey'),
    # postgresql_ignore_search_path=False
    # )
    # op.create_table('role',
    # sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('role_id_seq'::regclass)"), autoincrement=True, nullable=False),
    # sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    # sa.Column('permissions', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    # sa.PrimaryKeyConstraint('id', name='role_pkey'),
    # postgresql_ignore_search_path=False
    # )
    # op.create_table('resume',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('title', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    # sa.Column('compensation', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('workload', postgresql.ENUM('parttime', 'fulltime', name='workload'), autoincrement=False, nullable=False),
    # sa.Column('worker_id', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text("timezone('utc'::text, now())"), autoincrement=False, nullable=False),
    # sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text("timezone('utc'::text, now())"), autoincrement=False, nullable=False),
    # sa.ForeignKeyConstraint(['worker_id'], ['workers.id'], name='resume_worker_id_fkey', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('id', name='resume_pkey')
    # )
    # op.create_table('user',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.Column('registered_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    # sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    # sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    # sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    # sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='user_role_id_fkey'),
    # sa.PrimaryKeyConstraint('id', name='user_pkey')
    # )
    # op.create_table('operation',
    # sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    # sa.Column('quantity', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.Column('figi', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.Column('instrument_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    # sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.PrimaryKeyConstraint('id', name='operation_pkey')
    # )
    # op.drop_table('resumes')
    # op.drop_table('users_api')
    # ### end Alembic commands ###
