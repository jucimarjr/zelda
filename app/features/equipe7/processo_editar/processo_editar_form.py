from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


# Cadastra Processo
class EditarProcessoForm(Form):
    processo_tipo = StringField ('Tipo do Processo', validators=[DataRequired('O Tipo do Processo é obrigatório.')])
    processo_desc = TextAreaField('Descrição')

    