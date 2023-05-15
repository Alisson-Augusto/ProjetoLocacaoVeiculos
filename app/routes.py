from flask import Blueprint, flash, redirect, render_template, request
from flask_login import current_user, login_required
from app.forms.reserva import ReservaForm
from app.models.recibo import Recibo
from app.models.veiculos import Veiculos
from app.models.agencia import Agencia
from datetime import date
from app import db

rotas = Blueprint("rotas", __name__)


@rotas.route("/")
def home():
  veiculos = Veiculos.get_frota()
  return render_template("home/index.html", veiculos=veiculos)


@rotas.route("/conta")
@login_required
def perfil():
  recibos = current_user.get_historico_locacoes()
  return render_template("home/perfil.html", recibos=recibos)


@rotas.route("/agencias/veiculo/<modelo>", methods=["GET", "POST"])
@login_required
def agencias_veiculo(modelo):
  form = ReservaForm()
  agencias_retirada = Veiculos.get_agencias_com_modelo(modelo)
  
  if len(agencias_retirada) == 0:
    flash("Este veículo não esta mais disponível")
    return redirect("/")
  
  '''
  TODO - Lista de veículos deve ser atualizada
  Quando usuário troca de agência de retirada
  '''
  veiculos = Veiculos.get_from_agencia(agencias_retirada[0].id)
  agencias = Agencia.query.all()
  form.ag_retirada.choices = [(agencia.id, agencia.localizacao) for agencia in agencias_retirada]
  form.ag_devolucao.choices = [(agencia.id, agencia.localizacao) for agencia in agencias]
  form.veiculo.choices = [(veiculo.id, veiculo.get_nome()) for veiculo in veiculos]


  if form.validate_on_submit():
    # Realiza locação de veículo
    veiculo = form.veiculo.data
    dt_retirada = form.data_retirada.data
    dt_devolucao = form.data_devolucao.data

    recibo = Recibo(usuario=current_user.id,
                    veiculo=veiculo,
                    data_retirada=dt_retirada,
                    data_devolucao=dt_devolucao)
    
    db.session.add(recibo)
    # Remove virtualmente o veículo
    Veiculos.query.get(veiculo).disponibilidade = False  
    db.session.commit()
    return redirect("/")
  return render_template("agencia/agencia.html",
              form=form,
              data_atual=date.today())


@rotas.route("/agencias/<id>", methods=["GET", "POST"])
@login_required
def agencias(id):
  form = ReservaForm()
  agencia_selecionada = Agencia.query.get(id)
  agencias = Agencia.query.all()
  veiculos = Veiculos.get_from_agencia(id)
  form.ag_retirada.choices = [(id, agencia_selecionada.localizacao)]
  form.ag_devolucao.choices = [(agencia.id, agencia.localizacao) for agencia in agencias]
  form.veiculo.choices = [(veiculo.id, veiculo.get_nome()) for veiculo in veiculos]

  if form.validate_on_submit():
    # Realiza locação de veículo
    veiculo = form.veiculo.data
    dt_retirada = form.data_retirada.data
    dt_devolucao = form.data_devolucao.data

    recibo = Recibo(usuario=current_user.id,
                    veiculo=veiculo,
                    data_retirada=dt_retirada,
                    data_devolucao=dt_devolucao)
    
    db.session.add(recibo)
    # Remove virtualmente o veículo
    Veiculos.query.get(veiculo).disponibilidade = False  
    db.session.commit()
    return redirect("/")


  return render_template("agencia/agencia.html",
              form=form,
              data_atual=date.today())


@rotas.route("/agencias")
def buscar_agencia():
  busca = request.args.get("busca", "").strip()
  if busca == "":
    return []
  
  agencias = Agencia.query.filter(Agencia.localizacao.ilike(f"%{busca}%")).all()
  return [{"id": agencia.id, "localizacao": agencia.localizacao} for agencia in agencias]