from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_app() -> Flask:
  app = Flask(__name__)
  db.init_app(app)
  
  from .routes import rotas as rotas_blueprint
  app.register_blueprint(rotas_blueprint)

  return app