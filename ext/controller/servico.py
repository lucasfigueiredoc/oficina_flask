from flask import Blueprint, render_template, request, redirect, url_for
from ...database import db
from ..models import Servico
from ..models import Funcionario
from ..models import Carro
from ..form.servicoForm import ServicoForm

bp_servico = Blueprint("servico", __name__, template_folder="templates")

@bp_servico.route('/')
def recovery():
    servicos = db.session.query(Servico, Carro, Funcionario).\
        join(Carro, Servico.id_carro == Carro.id, isouter=True).\
        join(Funcionario, Servico.id_funcionario == Funcionario.id, isouter=True).\
        all()
    return render_template('list/list_servico.html', servicos=servicos)

@bp_servico.route('/create', methods=['GET', 'POST'])
def create():
    form = ServicoForm()
    form.set_choices()

    if request.method == 'POST' and form.validate_on_submit():
        novo_servico = Servico(
            descricao=form.descricao.data,
            id_carro=form.id_carro.data,
            id_funcionario=form.id_funcionario.data,
            data=form.data.data,
            status=form.status.data
        )

        db.session.add(novo_servico)
        db.session.commit()

        return redirect(url_for('servico.recovery'))

    return render_template('form/servico_form.html', form=form)

@bp_servico.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    s = Servico.query.get(id)
    form = ServicoForm(obj=s)

    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(s)
        db.session.commit()
        return redirect(url_for('servico.recovery'))

    return render_template('form/servico_form.html', form=form)

@bp_servico.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    s = Servico.query.get(id)

    if request.method == 'POST':
        db.session.delete(s)
        db.session.commit()

    return redirect(url_for('servico.recovery'))
