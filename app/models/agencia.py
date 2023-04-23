from app import db
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class Agencia(db.Model):
  __tablename__ = "agencias"
  id = sa.Column(sa.Integer, primary_key=True)
  localizacao = sa.Column(sa.String(500), nullable=False)
  nome = sa.Column(sa.String(144), nullable=False)
  funcionarios = relationship("Funcionario")
