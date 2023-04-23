from app import db
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class Funcionario(db.Model):
  __tablename__ = "funcionarios"
  id   = sa.Column(sa.Integer, primary_key=True)
  nome = sa.Column(sa.String(128), nullable=False)
  email = sa.Column(sa.String(128), nullable=False, unique=True)
  senha = sa.Column(sa.String(128), nullable=False, unique=True)
  nivel_acesso = sa.Column(sa.Integer, nullable=False)
  agencia = sa.Column(sa.Integer, sa.ForeignKey("agencias.id"))

  def __init__(self, **kwargs) -> None:
    super(Funcionario, self).__init__(**kwargs)
    self.senha = generate_password_hash(self.senha)

  def verificar_senha(self, senha: str) -> bool:
    return check_password_hash(self.senha, senha)

  def __repr__(self) -> str:
    return f"Funcionário: {self.nome} -> {self.id} - NIVEL({self.nivel_acesso})"
