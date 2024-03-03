from flask import Blueprint
from flask import render_template, request
from database import db
from .models import Funcionario

bp_funcionario = Blueprint("funcionario", __name__, template_folder="templates")

@bp_funcionario.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template('form/funcionario_form.html')

    if request.method=='POST':
        nome = request.form.get('nome')
        funcao = request.form.get('funcao')
        
        query = Funcionario(nome,funcao)
        
        db.session.add(query)
        db.session.commit()

        
    return render_template('form/funcionario.html')


@bp_funcionario.route('/')
def recovery():
    funcionario = funcionario.query.all()
    return render_template('list.html', value=funcionario)

@bp_funcionario.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    f = Funcionario.query.get(id)
    if request.method=='GET':

        return render_template('form/funcionario_form.html', value=f)
    
    if request.method=='POST':
        nome = request.form.get('nome')
        funcao = request.form.get('funcao')
        f.nome = nome
        f.funcao = funcao
        
        db.session.add(f)
        db.session.commit()
        
        
@bp_funcionario.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    f = Funcionario.query.get(id)

    if request.method=='POST':
        db.session.delete(f)
        db.session.commit()


