from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateField, PasswordField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    email = EmailField("email", validators=[InputRequired()])
    senha = PasswordField("senha", validators=[InputRequired()])
