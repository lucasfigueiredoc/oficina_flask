from flask import Blueprint
from flask import render_template, request
from ..form.funcionarioForm import FuncionarioForm
from ..models import Funcionario
from ...database import db

bp_funcionario = Blueprint("funcionario", __name__, template_folder="templates")
funcionario = Funcionario.query.all()
@bp_funcionario.route('/')
def recovery():
    funcionario = Funcionario.query.all()
    return render_template('list/list_funcionario.html', values=funcionario)

@bp_funcionario.route('/create', methods=['GET', 'POST'])
def create():
    funcionario = Funcionario.query.all()
    form = FuncionarioForm()
    if request.method=='GET':
        return render_template('form/funcionario_form.html', form=form)

    if form.validate_on_submit():
        nome = form.nome.data
        funcao = form.funcao.data
        
        novo_funcionario = Funcionario(nome=nome, funcao=funcao)
        
        db.session.add(novo_funcionario)
        db.session.commit()
        
        return render_template('list/list_funcionario.html', values=funcionario)

    return render_template('list/list_funcionario.html', values=funcionario)

@bp_funcionario.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    funcionario = Funcionario.query.all()
    f = Funcionario.query.get(id)
    form = FuncionarioForm(obj=f)
    if request.method=='GET':
        form.populate_obj(f)
        return render_template('form/funcionario_form.html', form=form)
    
    if form.validate_on_submit():
        form.populate_obj(f)
        db.session.commit()
        return render_template('list/list_funcionario.html', values=funcionario)
    return render_template('list/list_funcionario.html', values=funcionario)
        
@bp_funcionario.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    f = Funcionario.query.get(id)

    if request.method=='POST':
        db.session.delete(f)
        db.session.commit()
