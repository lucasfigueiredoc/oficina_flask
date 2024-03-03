from flask import Blueprint
from flask import render_template

bp_cliente = Blueprint("cliente", __name__, template_folder="templates")

@bp_cliente.route('/create')
def create():
    return render_template('cliente_create.html')

