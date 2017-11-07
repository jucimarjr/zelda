from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class ConfirmarEmailForm(Form):
    email = StringField('Email', validators = [DataRequired('Um endereço de email é obrigatório')])
    usuario_id = HiddenField('Id do Usuário', validators = [DataRequired('Usuário é obrigatório')])