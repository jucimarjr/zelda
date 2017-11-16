from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired

class CadastrarDocumentoForm(Form):
    documento_tipo = StringField('Tipo', validators=[DataRequired('Tipo do documento é obrigatório')])
    documento_desc = TextAreaField('Descrição')
