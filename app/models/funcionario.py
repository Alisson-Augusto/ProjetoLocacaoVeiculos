from app import db
import sqlalchemy as sa

class Fucionario(db.Model):
  __tablename__ = "funcionarios"
  id   = sa.Column(sa.Integer, primary_key=True)
  nome = sa.Column(sa.String(128), nullable=False)
  nivel_acesso = sa.Column(sa.Integer, nullable=False)

  def __repr__(self) -> str:
    return f"Funcionário: {self.nome} -> {self.id} - NIVEL({self.nivel_acesso})"
