from flask import Flask, Blueprint
from flask import render_template, request
from database import db
from ..form.carro_type import CarroForm
from ..model.models import Carro
from flask_wtf.csrf import CSRFProtect

bp_carro = Blueprint("carro", __name__, template_folder="templates")
app = Flask(__name__)
@app.route('/carro/create', methods=['GET', 'POST'])
def create():
    form = CarroForm()
    if request.method=='GET':
           return render_template('novo_carro.html', form=form)

    if form.validate_on_submit():
        
        novo_carro = Carro(
            marca=form.marca.data,
            placa=form.placa.data,
            modelo=form.modelo.data
        )
        
        db.session.add(novo_carro)
        db.session.commit()

    return render_template('novo_carro.html', form=form)

@bp_carro.route('/')
def recovery():
    carro = Carro.query.all()
    return render_template('list.html', values=carro)

@bp_carro.route('/update/<int:id>', methods=['GET', 'POST'])

    
def update(id):
    c = Carro.query.get(id)
    if request.method=='GET':

        return render_template('carro_form.html', value=c)
    
    if request.method=='POST':
        marca = request.form.get('marca')
        placa = request.form.get('placa')
        modelo = request.form.get('modelo')
        c.marca = marca
        c.placa = placa
        c.modelo = modelo
        
        db.session.add(c)
        db.session.commit()
        
    return render_template('index.html')

@bp_carro.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    c = Carro.query.get(id)

    if request.method=='POST':
        db.session.delete(c)
        db.session.commit()


