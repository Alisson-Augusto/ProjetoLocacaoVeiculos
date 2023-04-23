from app import db
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Funcionario(db.Model):
  __tablename__ = "funcionarios"
  id   = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
  nome = sa.Column(sa.String(128), nullable=False)
  nivel_acesso = sa.Column(sa.Integer, nullable=False)
  agencia = sa.Column(sa.ForeignKey("agencias.id"))

  def __repr__(self) -> str:
    return f"Funcionário: {self.nome} -> {self.id} - NIVEL({self.nivel_acesso})"
