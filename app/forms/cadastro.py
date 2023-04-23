from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateField, PasswordField
from wtforms.validators import InputRequired

class CadastroForm(FlaskForm):
    nome = StringField('nome', validators=[InputRequired()])
    email = EmailField("email", validators=[InputRequired()])
    senha = PasswordField("senha", validators=[InputRequired()])
    data_nascimento = DateField("data_nascimento", validators=[InputRequired()])
