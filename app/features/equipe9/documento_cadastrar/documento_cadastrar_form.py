from flask_wtf import Form
from wtforms import StringField, SelectField,TextField
from wtforms.validators import DataRequired, Required, EqualTo

# Cadastra Documento
class CadastrarDocumentoForm(Form):
    documento_tipo = StringField('Tipo Documento', validators=[DataRequired('Tipo do Documento é obrigatório')])
    documento_descricao = TextField('Descricao Documento', validators=[DataRequired('Descricao do Documento é obrigatório')])
    documento_caminho = StringField('Caminho Documento', validators=[DataRequired('Caminho do Documento é obrigatório')])
    documento_processo = SelectField('Processo Documento', validators=[DataRequired('Processo do Documento é obrigatório.')], coerce=int)
