from flask import Blueprint
from flask import render_template, request
from ..model.models import Cliente
from database import db

bp_cliente = Blueprint("cliente", __name__, template_folder="templates")

@bp_cliente.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template('form/cliente_form.html')

    if request.method=='POST':
        nome = request.form.get('nome')
        id_carro = request.form.get('id_carro')
        endereco = request.form.get('endereco')
        telefone = request.form.get('telefone')
        
        query = Cliente(nome, id_carro, endereco, telefone)
        
        db.session.add(query)
        db.session.commit()
        
    return render_template('cliente_create.html')

@bp_cliente.route('/')
def recovery():
    cliente = Cliente.query.all()
    return render_template('list.html', value=cliente)

@bp_cliente.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    c = Cliente.query.get(id)
    if request.method=='GET':

        return render_template('cliente_form.html', value=c)
    
    if request.method=='POST':
        nome = request.form.get('nome')
        id_carro = request.form.get('id_carro')
        endereco = request.form.get('endereco')
        telefone = request.form.get('telefone')
        c.nome = nome
        c.id_carro = id_carro
        c.endereco = endereco
        c.telefone = telefone
        
        db.session.add(c)
        db.session.commit()
        
        
@bp_cliente.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    c = Cliente.query.get(id)

    if request.method=='POST':
        db.session.delete(c)
        db.session.commit()


