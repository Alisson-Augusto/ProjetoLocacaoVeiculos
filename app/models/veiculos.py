from app import db
import sqlalchemy as sa

class Veiculos(db.Model):
  __tablename__ = "veiculos"
  id          = sa.Column(sa.Integer, primary_key=True)
  agencia     = sa.Column(sa.Integer, sa.ForeignKey("agencias.id"))
  diaria      = sa.Column(sa.Integer, nullable=False)
  descricao   = sa.Column(sa.String(128), nullable=False)
  imagem      = sa.Column(sa.String(50))
  modelo      = sa.Column(sa.String(50), nullable=False)
  marca       = sa.Column(sa.String(50), nullable=False)
  placa       = sa.Column(sa.String(8) , nullable=False, unique=True)
  ocupantes   = sa.Column(sa.Integer)
  porta_malas = sa.Column(sa.Integer)
  freio_abs   = sa.Column(sa.Boolean)
  disponibilidade = sa.Column(sa.Boolean, default=True)


  def get_imagem(self, placeholder = "images/car_placeholder.png") -> str:
    return self.imagem if self.imagem else placeholder 
  

  @staticmethod
  def __filtra_por_modelos(veiculos):
    resultado = []
    modelos = []
    for veiculo in veiculos:
      if not veiculo.modelo in modelos:
        resultado.append(veiculo)
        modelos.append(veiculo.modelo)
    return resultado


  @staticmethod
  def get_frota():
    return Veiculos.__filtra_por_modelos(Veiculos.query.all())
  

  @staticmethod
  def get_from_agencia(id):
    veiculos = Veiculos.query.filter(Veiculos.agencia==id, Veiculos.disponibilidade==True).all()
    return Veiculos.__filtra_por_modelos(veiculos)
  

  def get_nome(self) -> str:
    return f"{self.marca} - {self.modelo}"
  
  
  def __repr__(self) -> str:
    return f"Veículo[{self.placa}] - {self.modelo} da marca {self.marca}"