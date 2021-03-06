from flask_wtf import Form
from wtforms import StringField, PasswordField, HiddenField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Required, EqualTo
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Editar Documento
class EditarDocumentoForm(Form):
    documento_tipo = SelectField('Tipo', validators=[DataRequired('O Documento deve ter um tipo.')], coerce=int)
    documento_caminho = StringField('Caminho', validators=[DataRequired('O Documento precisa de um caminho para acesso.')])
    documento_descricao = TextAreaField('Descrição', validators=[DataRequired('O Documento deve ter uma descrição.')])