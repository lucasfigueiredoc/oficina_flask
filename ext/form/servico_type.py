from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired

class ServicoForm(FlaskForm):
    descricao = StringField('Descrição', validators=[DataRequired()])
    id_carro = IntegerField('ID do Carro', validators=[DataRequired()])
    id_funcionario = IntegerField('ID do Funcionário', validators=[DataRequired()])
    id_cliente = IntegerField('ID do Cliente', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()], format='%Y-%m-%d')
    status = SelectField('Status', choices=[(1, 'Ativo'), (2, 'Em Espera'), (3, 'Completo')], coerce=int, validators=[DataRequired()])
