from app import db
import sqlalchemy as sa

from app.models.veiculos import Veiculos

def formata_data(data) -> str:
  formata_tempo = lambda tempo: "0" + str(tempo) if tempo < 10 else str(tempo)
  dia: str = formata_tempo(data.day)
  mes: str = formata_tempo(data.month)
  ano: str = data.year
  return f"{dia}/{mes}/{ano}"


class Recibo(db.Model):
  __tablename__ = "recibo"
  id   = sa.Column(sa.Integer, primary_key=True)
  usuario = sa.Column(sa.Integer, sa.ForeignKey("usuarios.id"), nullable=False)
  veiculo = sa.Column(sa.Integer, sa.ForeignKey("veiculos.id"),nullable=False)
  data_retirada = sa.Column(sa.Date, nullable=False)
  data_devolucao = sa.Column(sa.Date, nullable=False)
  status_devolucao = sa.Column(sa.Boolean, nullable=False, default=False)


  def get_veiculo(self):
    return Veiculos.query.get(self.veiculo)

  
  def get_data_retirada(self) -> str:
    return formata_data(self.data_retirada)
  

  def get_data_devolucao(self) -> str:
    return formata_data(self.data_devolucao)


  def __repr__(self):
    return f"{self.usuario} -> alugou -> veiculo[{self.veiculo}]"
