from flask import Flask

def get_app() -> Flask:
  app = Flask(__name__)

  from .routes import rotas as rotas_blueprint
  app.register_blueprint(rotas_blueprint)

  return app