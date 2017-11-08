from flask_wtf import Form
from wtforms import StringField,PasswordField,TextField
from wtforms.validators import DataRequired, Required, EqualTo

class UsuarioSignupForm(Form):
    signup_login = StringField('Nome de Usuário',validators=[DataRequired('O nome de usuário é obrigatório')])
    signup_senha = PasswordField('Senha', validators=[DataRequired('A senha é obrigatória'), EqualTo('confirma_senha', message='As senhas devem ser iguais.')])
    confirma_senha = PasswordField('Confirmar Senha', validators=[Required()])
    signup_email = TextField("Email",  validators=[DataRequired("O seu email é obrigatório.")])
