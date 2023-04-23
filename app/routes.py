from flask import Blueprint, render_template

rotas = Blueprint("rotas", __name__)

@rotas.route("/")
def home():
  return render_template("home/index.html")


@rotas.route("/perfil")
def perfil():
  return render_template("home/perfil.html")


@rotas.route("/frota")
def frota():
  return render_template("home/frota.html")


@rotas.route("/admin")
def admin_page():
  return render_template("admin/admin.html")