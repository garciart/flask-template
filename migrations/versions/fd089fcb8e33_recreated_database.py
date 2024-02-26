"""Recreated database.

Revision ID: fd089fcb8e33
Revises: 
Create Date: 2024-02-25 19:42:45.310380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd089fcb8e33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('course_name', sa.String(length=64), nullable=False),
    sa.Column('course_code', sa.String(length=64), nullable=False),
    sa.Column('course_desc', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('course_id')
    )
    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_courses_course_code'), ['course_code'], unique=False)
        batch_op.create_index(batch_op.f('ix_courses_course_desc'), ['course_desc'], unique=False)
        batch_op.create_index(batch_op.f('ix_courses_course_name'), ['course_name'], unique=False)

    op.create_table('roles',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('role_id')
    )
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_roles_role_name'), ['role_name'], unique=True)

    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=64), nullable=False),
    sa.Column('user_group', sa.String(length=64), nullable=True),
    sa.Column('user_email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_user_email'), ['user_email'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_user_group'), ['user_group'], unique=False)
        batch_op.create_index(batch_op.f('ix_users_user_name'), ['user_name'], unique=True)

    op.create_table('associations',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'course_id', 'role_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('associations')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_user_name'))
        batch_op.drop_index(batch_op.f('ix_users_user_group'))
        batch_op.drop_index(batch_op.f('ix_users_user_email'))

    op.drop_table('users')
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roles_role_name'))

    op.drop_table('roles')
    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_courses_course_name'))
        batch_op.drop_index(batch_op.f('ix_courses_course_desc'))
        batch_op.drop_index(batch_op.f('ix_courses_course_code'))

    op.drop_table('courses')
    # ### end Alembic commands ###