from flask_wtf import Form
from wtforms import StringField,TextField, SelectField
from wtforms.validators import DataRequired
# Edita Processo
class EditarDocumentoForm(Form):
    documento_tipo = StringField('Tipo Processo', validators=[DataRequired('Tipo do Processo é obrigatório')])
    documento_descricao = TextField('Descricao Processo', validators=[DataRequired('Descricao do Processo é obrigatório')])
    documento_caminho = StringField('Caminho Processo', validators=[DataRequired('Caminho do Processo é obrigatório')])
    documento_processo = SelectField('Processo', coerce=int)
