from ..database import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from datetime import datetime

class Carro(db.Model, SerializerMixin):
    __tablename__ = "carro"
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(255), nullable=False)
    placa = db.Column(db.String(20), nullable=False, unique=True)
    modelo = db.Column(db.String(255), nullable=False)

    def __init__(self, marca, placa, modelo):
        self.marca = marca
        self.placa = placa
        self.modelo = modelo

class Funcionario(db.Model, SerializerMixin):
    __tablename__ = "funcionario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    funcao = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao

class Cliente(db.Model, SerializerMixin):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    id_carro = db.Column(db.Integer, db.ForeignKey('carro.id'))
    endereco = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    def __init__(self, nome, id_carro, endereco, telefone):
        self.nome = nome
        self.id_carro = id_carro
        self.endereco = endereco
        self.telefone = telefone

class Servico(db.Model, SerializerMixin):
    __tablename__ = "servico"
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    id_carro = db.Column(db.Integer, db.ForeignKey('carro.id'))
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id'))
    data = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, descricao, id_carro, id_funcionario, data, status):
        self.descricao = descricao
        self.id_carro = id_carro
        self.id_funcionario = id_funcionario
        self.data = data
        self.status = status
