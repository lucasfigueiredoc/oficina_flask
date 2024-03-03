from flask import Blueprint
from flask import render_template

bp_servico = Blueprint("servico", __name__, template_folder="templates")

@bp_servico.route('/create')
def create():
    return render_template('servico_create.html')

