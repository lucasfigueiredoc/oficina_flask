from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CarroForm(FlaskForm):
    marca = StringField('Marca', validators=[DataRequired()])
    placa = StringField('Placa', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    
    