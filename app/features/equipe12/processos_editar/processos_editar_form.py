from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired

class EditarProcessoForm(Form):
    processo_tipo = StringField('Tipo',validators=[DataRequired('Tipo do Processo é obrigatório')])
    processo_desc = TextAreaField('Descrição')
