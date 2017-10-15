from flask_wtf import Form
from wtforms import StringField,PasswordField,TextField
from wtforms.validators import DataRequired

class UsuarioSignupForm(Form):
    login = StringField('Nome de Usuário',validators=[DataRequired('O nome de usuário é obrigatório')])
    senha = PasswordField('Senha', validators=[DataRequired('A senha é obrigatória')])
    email = TextField("Email",  validators=[DataRequired("O seu email é obrigatório.")])
