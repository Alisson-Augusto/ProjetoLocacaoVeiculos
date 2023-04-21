from app import db
import sqlalchemy as sa

class Usuario(db.Model):
  __tablename__ = "usuarios"
  id   = sa.Column(sa.Integer, primary_key=True)
  nome = sa.Column(sa.String(128), nullable=False)
  data_nascimento = sa.Column(sa.Date, nullable=False)

  def __repr__(self) -> str:
    return f"{self.nome} -> {self.id} - DATA({self.data_nascimento})"
  