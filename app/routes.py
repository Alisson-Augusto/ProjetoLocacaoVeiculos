from flask import Blueprint, render_template

rotas = Blueprint("rotas", __name__)

@rotas.route("/")
def home():
  return render_template("index.html")


@rotas.route("/admin")
def admin_page():
  return render_template("admin/admin.html")