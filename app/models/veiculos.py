from app import db
import sqlalchemy as sa

class Veiculos(db.Model):
  __tablename__ = "veiculos"
  id     = sa.Column(sa.Integer, primary_key=True)
  modelo = sa.Column(sa.String(128), nullable=False)
  marca  = sa.Column(sa.String(128), nullable=False)
  disponibilidade = sa.Column(sa.Boolean, nullable=False)
  quantidade_ocupantes = sa.Column(sa.Integer, nullable=False)
  capacidade_porta_malas = sa.Column(sa.Integer)
  freio_abs = sa.Column(sa.Boolean)

  def __repr__(self) -> str:
    return f"Veículo - {self.modelo} da marca {self.marca} esta disponível? {self.disponibilidade}"