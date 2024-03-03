from flask import Blueprint
from flask import render_template, request
from .models import Carro
from database import db

bp_carro = Blueprint("carro", __name__, template_folder="templates")

@bp_carro.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template('carro_form.html')

    if request.method=='POST':
        marca = request.form.get('marca')
        placa = request.form.get('placa')
        modelo = request.form.get('modelo')
        
        query = Carro(marca, placa, modelo)
        
        db.session.add(query)
        db.session.commit()

    return render_template('carro_form.html')

@bp_carro.route('/')
def recovery():
    carro = Carro.query.all()
    return render_template('list.html', value=carro)

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

@bp_carro.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    c = Carro.query.get(id)

    if request.method=='POST':
        db.session.delete(c)
        db.session.commit()


