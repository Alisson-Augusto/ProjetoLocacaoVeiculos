from app import db
import sqlalchemy as sa

class Veiculos(db.Model):
  __tablename__ = "veiculos"
  id      = sa.Column(sa.Integer, primary_key=True)
  agencia = sa.Column(sa.Integer, sa.ForeignKey("agencias.id"))
  modelo  = sa.Column(sa.String(50), nullable=False)
  marca   = sa.Column(sa.String(50), nullable=False)
  placa   = sa.Column(sa.String(8) , nullable=False, unique=True)
  ocupantes = sa.Column(sa.Integer)
  porta_malas = sa.Column(sa.Integer)
  freio_abs = sa.Column(sa.Boolean)

  def __repr__(self) -> str:
    return f"Veículo[{self.placa}] - {self.modelo} da marca {self.marca}"