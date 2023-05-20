from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import DevConfig, TestConfig

db = SQLAlchemy()
login_manager = LoginManager()

def page_not_found(e):
  return render_template('error/404.html'), 404


def create_app(tipo="dev") -> Flask:
  app = Flask(__name__)
  if tipo == "test":
    app.config.from_object(TestConfig)
  else:
    app.config.from_object(DevConfig)

  db.init_app(app)
  login_manager.init_app(app)

  from .routes import rotas as rotas_blueprint
  from .autenticacao import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)
  app.register_blueprint(rotas_blueprint)
  app.register_error_handler(404, page_not_found)
  return app