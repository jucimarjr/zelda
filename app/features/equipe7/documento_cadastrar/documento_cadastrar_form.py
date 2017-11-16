from flask_wtf import Form
from wtforms import StringField, SelectField,TextAreaField
from wtforms.validators import DataRequired


# Cadastra Documento
class CadastrarDocumentoForm(Form):
    documento_tipo = StringField ('Tipo do Documento', validators=[DataRequired('O Tipo do Documento é obrigatório.')])
    documento_caminho = StringField('Caminho', validators=[DataRequired('O Documento precisa de um caminho para ser acessada.')])
    documento_desc = TextAreaField('Descrição')
    documento_processo = SelectField('Documento do Processo', validators=[DataRequired('Documento do Processo é obrigatório.')], coerce=int)
