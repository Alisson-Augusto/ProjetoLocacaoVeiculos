from flask import Blueprint

rotas = Blueprint("rotas", __name__)

@rotas.route("/")
def home():
  return "Olá mundo!"
