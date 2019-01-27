"""empty message

Revision ID: 3639883d8daa
Revises: e03623737f74
Create Date: 2019-01-27 15:45:17.882009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3639883d8daa'
down_revision = 'e03623737f74'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('image_url', sa.String(), nullable=True))
    op.drop_column('recipe', 'filename')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('filename', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('recipe', 'image_url')
    # ### end Alembic commands ###
