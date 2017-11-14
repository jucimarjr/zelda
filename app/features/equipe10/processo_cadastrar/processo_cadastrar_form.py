from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField
from wtforms import StringField, SelectMultipleField
from wtforms.validators import DataRequired

class CadastrarProcessoForm(Form):
    processo_tipo = TextAreaField('Tipo')
    processo_desc = TextAreaField('Descrição')
    funcionalidades_ids = SelectMultipleField('Documentos',
                                              validators=[DataRequired('Um documento é obrigatório')],
                                              coerce=int)
