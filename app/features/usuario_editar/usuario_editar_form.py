from flask_wtf import Form
from wtforms import StringField, PasswordField, HiddenField, RadioField, SelectField
from wtforms.validators import DataRequired, Required, EqualTo
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Editar Usuário
class EditarUsuarioForm(Form):
    usuario_login = StringField('Login do Usuário', validators=[DataRequired('Login do Usuário é obrigatório.')])
    usuario_senha = PasswordField('Senha do Usuário', validators=[Required('A senha do Usuário é obrigatória.'), EqualTo('confirma_senha', message='As senhas devem ser iguais.')])
    confirma_senha = PasswordField('Confirmar Senha', validators=[Required('Confirmação de senha obrigatória.')])
    usuario_perfil = SelectField('Perfil', coerce=int)
    file = FileField('Foto do Usuário', validators=[])
