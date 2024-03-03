from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    id_carro = IntegerField('ID do Carro', validators=[DataRequired()])
    endereco = StringField('Endereço', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
