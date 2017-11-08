from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Required, EqualTo

class UsuarioRecuperarSenhaEmailForm(Form):
	recupera_email = StringField('Email', validators = [DataRequired('O email é obrigatório')])

class UsuarioNovaSenha(Form):
	nova_senha = PasswordField('Senha', validators = [DataRequired('A Senha do Usuario é obrigatória.'), EqualTo('confirma_senha', message='As senhas devem ser iguais.')])
	confirma_senha = PasswordField('Confirmar Senha', validators=[Required()])
