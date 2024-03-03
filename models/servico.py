from flask import Blueprint
from flask import render_template, request
from database import db
from .models import Servico

bp_servico = Blueprint("servico", __name__, template_folder="templates")

@bp_servico.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template('form/servico_form.html')

    if request.method=='POST':
        descricao = request.form.get('descricao')
        id_carro = request.form.get('id_Carro')
        id_funcionario = request.form.get('id_Funcionario')
        id_cliente = request.form.get('id_Cliente')
        data = request.form.get('data')
        status = request.form.get('status')
        
        
        query = Servico(descricao, id_carro, id_funcionario, id_cliente, data, status)
        
        db.session.add(query)
        db.session.commit()

        
    return render_template('form/servico.html')


@bp_servico.route('/')
def recovery():
    servico = servico.query.all()
    return render_template('list.html', value=servico)

@bp_servico.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    s = Servico.query.get(id)
    if request.method=='GET':

        return render_template('form/servico_form.html', value=s)
    
    if request.method=='POST':
        descricao = request.form.get('descricao')
        id_carro = request.form.get('id_Carro')
        id_funcionario = request.form.get('id_Funcionario')
        id_cliente = request.form.get('id_Cliente')
        data = request.form.get('data')
        status = request.form.get('status')
        
        s.descricao = descricao
        s.id_carro = id_carro
        s.id_funcionario = id_funcionario
        s.id_cliente = id_cliente
        s.data = data
        s.status = status
        
        db.session.add(s)
        db.session.commit()
        
        
@bp_servico.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    s = Servico.query.get(id)

    if request.method=='POST':
        db.session.delete(s)
        db.session.commit()


