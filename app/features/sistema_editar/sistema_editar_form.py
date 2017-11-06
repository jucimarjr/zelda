from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class EditarSistemaForm(Form):
    sistema_nome = StringField('Nome', validators=[DataRequired('Nome do Sistema é obrigatório')])
    sistema_desc = TextAreaField('Descrição')
    sistema_prefixo = StringField('Prefixo', validators = [DataRequired('Prefixo do Sistema é obrigatório')])