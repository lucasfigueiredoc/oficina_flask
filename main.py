from flask import Flask, render_template
from .database import db
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from .ext.model.models import bp_cliente, Cliente
from .ext.model.models import bp_funcionario, Funcionario
from .ext.model.models import bp_servico, Servico
from .ext.model.models import bp_carro, Carro

app = Flask(__name__)

# Database
connect =  "sqlite:///oficina.sqlite"
app.config['SECRET_KEY'] = 'root'
app.config['SQLALCHEMY_DATABASE_URI'] = connect
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

# Blueprints
app.register_blueprint(bp_carro, url_prefix='/carro')
app.register_blueprint(bp_cliente, url_prefix='/cliente')
app.register_blueprint(bp_funcionario, url_prefix='/funcionario')
app.register_blueprint(bp_servico, url_prefix='/servico')


Bootstrap(app)

@app.route('/')
def index():
    values = Servico.query.join(Funcionario).join(Carro).join(Cliente).all()
    return render_template('index.html', values=values)

if __name__ == "__main__":
    app.run(debug=True)