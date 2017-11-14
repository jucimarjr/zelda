from flask_wtf import Form
from wtforms import SelectField, TextAreaField, StringField
from wtforms.validators import DataRequired

class DocumentoCadastrarForm(Form):
    documento_tipo = SelectField('Tipo', validators=[DataRequired('O Documento deve ter um tipo.')], coerce=int)
    documento_caminho = StringField('Caminho', validators=[DataRequired('O Documento precisa de um caminho para ser acessada.')])
    documento_desc = TextAreaField('Descrição', validators=[DataRequired('O Documento deve ter uma descrição.')])