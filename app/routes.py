from flask import Blueprint, render_template, request

from app.models.veiculos import Veiculos
from app.models.agencia import Agencia
from datetime import date

rotas = Blueprint("rotas", __name__)

@rotas.route("/")
def home():
  veiculos = Veiculos.get_frota()
  return render_template("home/index.html", veiculos=veiculos)


@rotas.route("/perfil")
def perfil():
  return render_template("home/perfil.html")


@rotas.route("/agencias/<id>")
def agencias(id):
  agencia_selecionada = Agencia.query.get(id)
  agencias = Agencia.query.all()
  return render_template("agencia/agencia.html", agencia_selecionada=agencia_selecionada, agencias=agencias, data_atual=date.today())


@rotas.route("/agencias")
def buscar_agencia():
  busca = request.args.get("busca", "").strip()
  if busca == "":
    return []
  
  agencias = Agencia.query.filter(Agencia.localizacao.ilike(f"%{busca}%")).all()
  return [{"id": agencia.id, "localizacao": agencia.localizacao} for agencia in agencias]