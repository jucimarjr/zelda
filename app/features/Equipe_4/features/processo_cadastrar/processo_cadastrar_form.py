from flask_wtf import Form
from wtforms import StringField, TextAreaField,SelectField
from wtforms.validators import DataRequired


# Cadastra Processo
class CadastrarProcessoForm(Form):
    processo_tipo = StringField ('Tipo do Processo', validators=[DataRequired('O Tipo do Processo é obrigatório.')])
    processo_desc = TextAreaField('Descrição')
    usuario = SelectField('Usuário', validators=[DataRequired('Usuário é obrigatório')], coerce = int)    
