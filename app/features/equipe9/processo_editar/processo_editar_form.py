from flask_wtf import Form
from wtforms import StringField, TextField, SelectField
from wtforms.validators import DataRequired
# Edita Processo
class EditarProcessoForm(Form):
    processo_tipo = StringField('Tipo Processo', validators=[DataRequired('Tipo do Processo é obrigatório')])
    processo_descricao = TextField('Descricao Processo', validators=[DataRequired('Descricao do Processo é obrigatório')])
    processo_usuario = SelectField('Usuario', coerce=int)
