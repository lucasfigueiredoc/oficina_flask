from database import db, Integer, String, Column
from sqlalchemy_serializer import SerializerMixin

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
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
    def __init__(self, nome, placa, funcao):
        self.nome = nome
        self.placa = placa
        self.funcao = funcao

class Cliente(db.Model, SerializerMixin):
    __tablename__="cliente"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    id_carro = db.Column(db.String, db.ForeignKey('carro.id'))
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
    
    def __init__(self, nome, placa, id_carro):
        self.nome = nome
        self.placa = placa
        self.id_carro = id_carro
    

class Servico(db.Model, SerializerMixin):
    __tablename__="servico"
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(String, nullable=False)
    id_Carro = db.Column(db.Integer, db.ForeignKey('carro.id'))
    id_Funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id'))
    id_Cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    data = db.Column(db.Date)
    status = db.Column(Integer, nullable=False)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
    
    def __init__(self, descricao, id_carro, id_funcionario, id_cliente, data, status):
        self.descricao = descricao
        self.id_carro = id_carro
        self.id_funcionario = id_funcionario
        self.id_cliente = id_cliente
        self.data = data
        self.status = status
