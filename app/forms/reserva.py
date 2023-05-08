from flask_wtf import FlaskForm
from wtforms import SelectField, DateField
from wtforms.validators import InputRequired


class ReservaForm(FlaskForm):
  ag_retirada   = SelectField("Agência de Retirada", coerce=int, validators=[InputRequired()])
  data_retirada = DateField("data_retirada", validators=[InputRequired()])

  ag_devolucao   = SelectField("Agência de Devolução", coerce=int, validators=[InputRequired()])
  data_devolucao = DateField("data_devolucao", validators=[InputRequired()])
  veiculo = SelectField("Escolha o veículo", coerce=int, validators=[InputRequired()])
  
  def __repr__(self) -> str:
    text_retirada  = f"Agência: {self.ag_retirada.data}\n\tData: {self.data_retirada.data}"
    text_devolucao = f"Agência: {self.ag_devolucao.data}\n\tData: {self.data_devolucao.data}"
    return f"Reservar:\n\t{text_retirada}\nDevolucao\n\t{text_devolucao}"