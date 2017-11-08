from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField,TextField
from wtforms.validators import DataRequired, Required, EqualTo
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Cadastra Usuario
class CadastrarUsuarioForm(Form):
    usuario_login = StringField('Login Usuario', validators=[DataRequired('Login do Usuario é obrigatório.')])
    usuario_email = TextField("Email",  validators=[DataRequired("O seu email é obrigatório.")])
    usuario_senha = PasswordField('Senha', validators=[DataRequired('A Senha do Usuario é obrigatória.'), EqualTo('confirma_senha', message='As senhas devem ser iguais.')])
    confirma_senha = PasswordField('Confirmar Senha', validators=[Required()])
    usuario_perfil = SelectField('Perfil do Usuário', validators=[DataRequired('Perfil do Usuário é obrigatório.')], coerce=int)
    file = FileField('Foto do Usuário', validators=[])
