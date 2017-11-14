from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Cadastra Processos
class CadastrarProcessoForm(Form):
    processo_tipo = StringField('Tipo',validators=[DataRequired('Tipo do Processo é obrigatório')])
    processo_desc = TextAreaField('Descrição')
