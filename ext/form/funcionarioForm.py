from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class FuncionarioForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    funcao = StringField('Função', validators=[DataRequired()])
