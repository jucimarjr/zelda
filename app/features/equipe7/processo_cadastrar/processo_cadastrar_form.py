from flask_wtf import Form
from wtforms import StringField, SelectField,TextAreaField
from wtforms.validators import DataRequired


# Cadastra Processo
class CadastrarProcessoForm(Form):
    processo_tipo = StringField ('Tipo do Processo', validators=[DataRequired('O Tipo do Processo é obrigatório.')])
    processo_desc = TextAreaField('Descrição')
    processo_usuario = SelectField('Usuário do Processo', validators=[DataRequired('Usuário do Processo é obrigatório.')], coerce=int)

    