from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import pymysql


## Inicialização da aplicação via flask
app = Flask(__name__)
app.config.from_object('config')

pymysql.install_as_MySQLdb()

# Inicialização da conexão e migration para o banco
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Migrations: Controlam mudanças no banco de dados (ex: criar/alterar tabelas)
# Sincronizam o banco com o código, mantendo a estrutura sempre atualizada
migrate = Migrate(app, db)

# Construção da api através da utilização da aplicação em flasl
api = Api(app)

