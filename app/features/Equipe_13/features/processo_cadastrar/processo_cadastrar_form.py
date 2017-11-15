from flask_wtf import Form
from wtforms import StringField, SelectField,TextAreaField
from wtforms.validators import DataRequired

class ProcessoCadastrarForm(Form):
    processo_tipo = StringField ('Tipo do Processo', validators=[DataRequired('O Tipo do Processo é obrigatório.')])
    processo_descricao = TextAreaField('Descrição')




