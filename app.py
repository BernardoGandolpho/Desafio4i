# Flask e SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria a aplicação utilizando Flask
def create_app():
    app = Flask(__name__)
    config_app(app)

    return app

# Configura a aplicação
def config_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


# Cria o banco de dados da aplicação 
def create_db(app):
    db = SQLAlchemy(app)
    
    return db
