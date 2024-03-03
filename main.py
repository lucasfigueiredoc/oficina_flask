from flask import Flask, render_template
from database import db
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from models.cliente import bp_cliente
from models.funcionario import bp_funcionario
from models.servico import bp_servico
from models.carro import bp_carro

app = Flask(__name__)
connect =  "sqlite:///oficina.sqlite"
app.config['SECRET_KEY'] = 'root'
app.config['SQLALCHEMY_DATABASE_URI'] = connect
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

app.run()
