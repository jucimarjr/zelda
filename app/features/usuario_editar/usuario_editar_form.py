from flask_wtf import Form
from wtforms import StringField, PasswordField, HiddenField, RadioField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Editar Usuário
class EditarUsuarioForm(Form):
    usuario_login = StringField('Login do Usuário', validators=[DataRequired('Login do Usuário é obrigatório')])
    usuario_id = HiddenField('ID Usuário', validators=[DataRequired('O ID do Usuário não pode ser indefinido')])
    usuario_senha = PasswordField('Senha do Usuário', validators=[DataRequired('A senha do Usuário é obrigatória')])
    usuario_perfil = SelectField('Perfil', coerce=int)
    file = FileField('Foto do Usuário', validators=[])
