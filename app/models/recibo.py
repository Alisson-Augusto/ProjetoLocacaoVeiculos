from app import db
import sqlalchemy as sa

class Recibo(db.Model):
  __tablename__ = "recibo"
  id   = sa.Column(sa.Integer, primary_key=True)
  usuario = sa.Column(sa.Integer, sa.ForeignKey("usuarios.id"), nullable=False)
  veiculo = sa.Column(sa.Integer, sa.ForeignKey("veiculos.id"), nullable=False)
  data_retirada = sa.Column(sa.Date, nullable=False)
  data_devolucao = sa.Column(sa.Date, nullable=False)
  status_devolucao = sa.Column(sa.Boolean, nullable=False, default=False)

  def __repr__(self):
    return f"{self.usuario} -> alugou -> veiculo[{self.veiculo}]"
