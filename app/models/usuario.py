from app import db
import sqlalchemy as sa
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.recibo import Recibo

class Usuario(UserMixin, db.Model):
  __tablename__ = "usuarios"
  id   = sa.Column(sa.Integer, primary_key=True)
  nome = sa.Column(sa.String(128), nullable=False)
  email = sa.Column(sa.String(128), nullable=False, unique=True)
  senha = sa.Column(sa.String(120), nullable=False)
  data_nascimento = sa.Column(sa.Date, nullable=False)

  def __init__(self, **kwargs) -> None:
    super(Usuario, self).__init__(**kwargs)
    self.senha = generate_password_hash(self.senha)

  def verificar_senha(self, senha: str) -> bool:
    return check_password_hash(self.senha, senha)
  
  def get_historico_locacoes(self):
    return Recibo.query.filter(Recibo.usuario==self.id).order_by(Recibo.data_retirada.desc()).all()

  def __repr__(self) -> str:
    return f"{self.nome} -> {self.email} -> {self.id} -> DATA({self.data_nascimento})"
  