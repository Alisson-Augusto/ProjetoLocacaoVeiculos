from flask import Blueprint, flash, redirect, render_template
from flask_login import login_required, login_user, logout_user

from app.forms.login import LoginForm
from .forms.cadastro import CadastroForm
from app.models.usuario import Usuario 
from app import login_manager, db


auth = Blueprint("autenticacao", __name__)


@login_manager.user_loader
def load_user(user_id):
  return Usuario.query.get(user_id)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        usuario:Usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verificar_senha(form.senha.data):
            login_user(usuario)
            return redirect("/")
        flash("Email ou senha incorreto")

    return render_template("auth/login.html", form=form)


@auth.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        email = form.email.data
        usuario:Usuario = Usuario.query.filter_by(email=email).first()
        if not usuario:
            # Registra usuário no banco
            user = Usuario(
                nome=form.nome.data,
                email=email,
                senha=form.senha.data,
                data_nascimento=form.data_nascimento.data
                )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect("/")
        
        flash("Este usuário já foi cadastrado")
    return render_template("auth/cadastro.html", form=form)


@auth.route("/deslogar")
@login_required
def deslogar():
    logout_user()
    return redirect("/")