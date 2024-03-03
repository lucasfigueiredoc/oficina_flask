from flask import Blueprint
from flask import render_template, request
from .models import Carro
from database import db

bp_carro = Blueprint("carro", __name__, template_folder="templates")

@bp_carro.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template('funcionario_create.html')

    if request.method=='POST':
        marca = request.form.get('marca')
        placa = request.form.get('placa')
        modelo = request.form.get('modelo')
        
        query = Carro(marca, placa, modelo)
        
        db.session.add(query)
        db.session.commit()

    return render_template('carro_create.html')

    