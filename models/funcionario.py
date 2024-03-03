from flask import Blueprint
from flask import render_template

bp_funcionario = Blueprint("funcionario", __name__, template_folder="templates")

@bp_funcionario.route('/create', methods=['GET', 'POST'])
def create():
    
    return render_template('funcionario_create.html')

