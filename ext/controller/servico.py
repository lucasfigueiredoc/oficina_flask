from flask import Blueprint
from flask import render_template, request
from ...database import db
from ..models import Servico
from ..form.servicoForm import ServicoForm

bp_servico = Blueprint("servico", __name__, template_folder="templates")

@bp_servico.route('/')
def recovery():
    servico = servico.query.all()
    return render_template('list.html', value=servico)

@bp_servico.route('/create', methods=['GET', 'POST'])
def create():
    form = ServicoForm()
    if request.method=='GET':
        form.set_choices()
        return render_template('form/servico_form.html', form=form)

    if form.validate_on_submit():
        descricao = form.descricao.data
        id_carro = form.id_carro.data
        id_funcionario = form.id_funcionario.data
        data = form.data.data
        status = form.status.data
        
        novo_servico = Servico(descricao=descricao, id_carro=id_carro, id_funcionario=id_funcionario, data=data, status=status)
        
        db.session.add(novo_servico)
        db.session.commit()
        
    return render_template('form/servico_form.html')

@bp_servico.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    s = Servico.query.get(id)
    form = ServicoForm(obj=s)
    if request.method=='GET':
        form.populate_obj(s)
        return render_template('form/servico_form.html', form=form)
    
    if form.validate_on_submit():
        form.populate_obj(s)
        db.session.commit()
        return render_template('list/list_servico.html')
    
    return render_template('list/list_servico.html')
        
        
@bp_servico.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    s = Servico.query.get(id)

    if request.method=='POST':
        db.session.delete(s)
        db.session.commit()
