from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

# Cadastra Login
class LoginForm(Form):
    login = StringField('Nome de Usuário', validators=[DataRequired('O nome de usuário é obrigatório')])
    senha = PasswordField('Senha', validators=[DataRequired('A senha é obrigatória')])