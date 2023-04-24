from flask import Blueprint, render_template

from app.models.veiculos import Veiculos

rotas = Blueprint("rotas", __name__)

@rotas.route("/")
def home():
  veiculos = Veiculos.get_frota()
  return render_template("home/index.html", veiculos=veiculos)


@rotas.route("/perfil")
def perfil():
  return render_template("home/perfil.html")


@rotas.route("/admin")
def admin_page():
  return render_template("admin/admin.html")