# carro_blueprint.py
from flask import Blueprint, render_template, request, redirect, url_for
from ...database import db
from ..form.carroForm import CarroForm
from ..models import Carro

bp_carro = Blueprint("carro", __name__, template_folder="templates")
carros = Carro.query.all()
@bp_carro.route('/')
def recovery():
    carros = Carro.query.all()
    return render_template('list/list_carro.html', values=carros)

@bp_carro.route('/create', methods=['GET', 'POST'])
def create():

    form = CarroForm()
    if request.method == 'GET':
        return render_template('form/carro_form.html', form=form)

    if form.validate_on_submit():
        novo_carro = Carro(
            marca=form.marca.data,
            placa=form.placa.data,
            modelo=form.modelo.data
        )

        db.session.add(novo_carro)
        db.session.commit()
        return render_template('list/list_carro.html', values=carros)

    return render_template('list/list_carro.html', values=carros)

@bp_carro.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    carro = Carro.query.get(id)
    if request.method == 'GET':
        return render_template('form/carro_form.html', form=CarroForm(obj=carro))

    if request.method == 'POST':
        form = CarroForm(request.form)
        if form.validate():
            form.populate_obj(carro)
            db.session.commit()
            return redirect(url_for('carro.recovery'))

    return render_template('form/carro_form.html', form=CarroForm(obj=carro))

@bp_carro.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    carro = Carro.query.get(id)
    db.session.delete(carro)
    db.session.commit()
    return redirect(url_for('carro.recovery'))
