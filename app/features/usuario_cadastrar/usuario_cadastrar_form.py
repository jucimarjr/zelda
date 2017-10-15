from flask_wtf import Form
from wtforms import StringField, PasswordField, RadioField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Cadastra Usuario
class CadastrarUsuarioForm(Form):
    usuario_login = StringField('Login Usuario', validators=[DataRequired('Login do Usuario é obrigatório')])
    usuario_senha = PasswordField('Senha', validators=[DataRequired('Senha do Usuario é obrigatório')])
    usuario_admin = RadioField('Tipo do Usuário', validators=[DataRequired('Tipo do Usuário é obrigatório')], choices=[(1, 'Administrador'), (2, 'Usuário Comum')], coerce=int)
    file = FileField('Foto do Usuário', validators=[])
