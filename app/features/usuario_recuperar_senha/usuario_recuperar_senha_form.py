from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class UsuarioRecuperarSenhaEmailForm(Form):
	recupera_email = StringField('Email', validators = [DataRequired('O email é obrigatório')])

class UsuarioNovaSenha(Form):
	nova_senha = PasswordField('Senha', validators = [DataRequired()])
