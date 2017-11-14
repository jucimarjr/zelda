from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired

class CadastrarDocumentoForm(Form):
    documento_tipo = TextAreaField('Tipo', validators=[DataRequired('Um tipo é obrigatório')])
    documento_desc = TextAreaField('Descrição', validators=[DataRequired('Uma descrição é obrigatória')])
    file = FileField('Imagem do documento', validators=[])