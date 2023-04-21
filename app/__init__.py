from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

db = SQLAlchemy()

def page_not_found(e):
  return render_template('error/404.html'), 404

def get_app() -> Flask:
  app = Flask(__name__)
  app.config.from_object(DevConfig)
  db.init_app(app)
  
  from .routes import rotas as rotas_blueprint
  app.register_blueprint(rotas_blueprint)
  app.register_error_handler(404, page_not_found)
  return app