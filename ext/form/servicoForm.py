from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired
from ..models import Carro
from ..models import Funcionario
from ..models import Cliente

class ServicoForm(FlaskForm):
    descricao = StringField('Descrição', validators=[DataRequired()])
    id_carro = SelectField('ID do Carro', validators=[DataRequired()])
    id_funcionario = SelectField('ID do Funcionário', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()], format='%Y-%m-%d')
    status = SelectField('Status', choices=[(1, 'Ativo'), (2, 'Em Espera'), (3, 'Completo')], coerce=int, validators=[DataRequired()])


    def set_choices(self):
        carros = Carro.query.all()
        funcionarios = Funcionario.query.all()
        
        self.id_carro.choices = [(carro.id, f"{carro.marca} {carro.modelo} - Placa: {carro.placa}") for carro in carros]
        self.id_funcionario.choices = [(funcionario.id, f"{funcionario.nome} - Função {funcionario.nome} ") for funcionario in funcionarios]       