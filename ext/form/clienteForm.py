from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired
from ..models import Carro

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    id_carro = SelectField('ID do Carro', validators=[DataRequired()])
    endereco = StringField('Endereço', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    
    
    def set_choices(self):
        carros = Carro.query.all()
        self.id_carro.choices = [(carro.id, f"{carro.marca} {carro.modelo} - Placa: {carro.placa}") for carro in carros]
