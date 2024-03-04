from flask import Blueprint
from flask import render_template, request
from ..form.clienteForm import ClienteForm
from ..models import Carro
from ..models import Cliente
from ...database import db

bp_cliente = Blueprint("cliente", __name__, template_folder="templates")

@bp_cliente.route('/')
def recovery():
    cliente = Cliente.query.join(Carro).all()
    
    return render_template('list/list_cliente.html', values=cliente)

@bp_cliente.route('/create', methods=['GET', 'POST'])
def create():
    form = ClienteForm()
    form.set_choices()
    if request.method=='GET':
        return render_template('form/cliente_form.html', form=form)

    if form.validate_on_submit():
        nome = form.nome.data
        id_carro = form.id_carro.data
        endereco = form.endereco.data
        telefone = form.telefone.data
        
        novo_cliente = Cliente(nome=nome, id_carro=id_carro, endereco=endereco, telefone=telefone)

        db.session.add(novo_cliente)
        db.session.commit()
            
        return render_template('list/list_cliente.html', form=form)

@bp_cliente.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    c = Cliente.query.get(id)
    form = ClienteForm(obj=c)
    
    if request.method=='GET':
        form.populate_obj(c)
        return render_template('form/cliente_form.html', form=form)
    
    if form.validate_on_submit():
        form.populate_obj(c)
        db.session.commit()
        
    return render_template('list/list_cliente.html')
        
@bp_cliente.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    c = Cliente.query.get(id)

    if request.method=='POST':
        db.session.delete(c)
        db.session.commit()
