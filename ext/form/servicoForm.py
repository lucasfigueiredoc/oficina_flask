from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from ..models import Carro, Funcionario

class ServicoForm(FlaskForm):
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    id_carro = SelectField('ID do Carro', validators=[DataRequired()])
    id_funcionario = SelectField('ID do Funcionário', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()], format='%Y-%m-%d')
    status = SelectField('Status', coerce=int, validators=[DataRequired()])

    def set_choices(self):
        carros = Carro.query.all()
        funcionarios = Funcionario.query.all()

        self.status.choices = [(1, 'Ativo'), (2, 'Em Espera'), (3, 'Completo')]
        self.id_carro.choices = [(carro.id, f"{carro.marca} {carro.modelo} - Placa: {carro.placa}") for carro in carros]
        self.id_funcionario.choices = [(funcionario.id, f"{funcionario.nome} - Função: {funcionario.funcao}") for funcionario in funcionarios]
