"""add created_by and updated_by to app, modelconfig, and site

Revision ID: d0187d6a88dd
Revises: 675b5321501b
Create Date: 2024-08-25 04:41:18.157397

"""

import sqlalchemy as sa
from alembic import op

import models as models

# revision identifiers, used by Alembic.
revision = "d0187d6a88dd"
down_revision = "675b5321501b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("app_model_configs", schema=None) as batch_op:
        batch_op.add_column(sa.Column("created_by", models.types.StringUUID(), nullable=True))
        batch_op.add_column(sa.Column("updated_by", models.types.StringUUID(), nullable=True))

    with op.batch_alter_table("apps", schema=None) as batch_op:
        batch_op.add_column(sa.Column("created_by", models.types.StringUUID(), nullable=True))
        batch_op.add_column(sa.Column("updated_by", models.types.StringUUID(), nullable=True))

    with op.batch_alter_table("sites", schema=None) as batch_op:
        batch_op.add_column(sa.Column("created_by", models.types.StringUUID(), nullable=True))
        batch_op.add_column(sa.Column("updated_by", models.types.StringUUID(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("sites", schema=None) as batch_op:
        batch_op.drop_column("updated_by")
        batch_op.drop_column("created_by")

    with op.batch_alter_table("apps", schema=None) as batch_op:
        batch_op.drop_column("updated_by")
        batch_op.drop_column("created_by")

    with op.batch_alter_table("app_model_configs", schema=None) as batch_op:
        batch_op.drop_column("updated_by")
        batch_op.drop_column("created_by")

    # ### end Alembic commands ###