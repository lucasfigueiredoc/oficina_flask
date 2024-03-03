"""Initial migration.

Revision ID: 9de92c0d146c
Revises: 
Create Date: 2024-03-03 14:06:29.923004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9de92c0d146c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('marca', sa.String(), nullable=False),
    sa.Column('placa', sa.String(), nullable=False),
    sa.Column('modelo', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('funcionario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('funcao', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('id_carro', sa.String(), nullable=True),
    sa.Column('endereco', sa.String(), nullable=False),
    sa.Column('telefone', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_carro'], ['carro.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('servico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(), nullable=False),
    sa.Column('id_Carro', sa.Integer(), nullable=True),
    sa.Column('id_Funcionario', sa.Integer(), nullable=True),
    sa.Column('id_Cliente', sa.Integer(), nullable=True),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_Carro'], ['carro.id'], ),
    sa.ForeignKeyConstraint(['id_Cliente'], ['cliente.id'], ),
    sa.ForeignKeyConstraint(['id_Funcionario'], ['funcionario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('servico')
    op.drop_table('cliente')
    op.drop_table('funcionario')
    op.drop_table('carro')
    # ### end Alembic commands ###