"""empty message

Revision ID: df7babc4193e
Revises: 54cfdf51870e
Create Date: 2023-08-27 13:12:18.548170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df7babc4193e'
down_revision = '54cfdf51870e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deck',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('dateCreated', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phone',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('address', sa.VARCHAR(length=75), nullable=False),
    sa.Column('phoneNum', sa.VARCHAR(length=75), nullable=False),
    sa.Column('dateCreated', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('phoneNum')
    )
    op.drop_table('deck')
    # ### end Alembic commands ###