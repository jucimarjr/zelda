from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class CadastrarSistemaForm(Form):
    sistema_nome = StringField('Nome', validators=[DataRequired('Nome do Sistema é obrigatório')])
    sistema_desc = TextAreaField('Descrição')
    sistema_status = SelectField('Status', validators=[DataRequired('Status do Sistema')], coerce=int)
    sistema_prefixo = StringField('Prefixo', validators = [DataRequired('Prefixo do Sistema é obrigatório')])