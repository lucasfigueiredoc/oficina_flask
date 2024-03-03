from ...database import db, Integer, String, Column
from sqlalchemy_serializer import SerializerMixin
from wtforms.validators import DataRequired

class Carro(db.Model, SerializerMixin):
    __tablename__="carro"
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String, nullable=False)
    placa = db.Column(db.String, nullable=False)
    modelo = db.Column(db.String, nullable=False)
    
    def __init__(self, marca, placa, modelo):
        self.marca = marca
        self.placa = placa
        self.modelo = modelo
    
class Funcionario(db.Model, SerializerMixin):
    __tablename__="funcionario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    funcao = db.Column(db.String, nullable=False)

    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao

class Cliente(db.Model, SerializerMixin):
    __tablename__="cliente"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    id_carro = db.Column(db.String, db.ForeignKey('carro.id'))
    endereco = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String, nullable=False)
    
    def __init__(self, nome, id_carro, endereco, telefone):
        self.nome = nome
        self.id_carro = id_carro
        self.endereco = endereco
        self.telefone = telefone

class Servico(db.Model, SerializerMixin):
    __tablename__="servico"
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(String, nullable=False)
    id_Carro = db.Column(db.Integer, db.ForeignKey('carro.id'))
    id_Funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id'))
    id_Cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    data = db.Column(db.Date)
    status = db.Column(Integer, nullable=False)
    
    def __init__(self, descricao, id_carro, id_funcionario, id_cliente, data, status):
        self.descricao = descricao
        self.id_carro = id_carro
        self.id_funcionario = id_funcionario
        self.id_cliente = id_cliente
        self.data = data
        self.status = status