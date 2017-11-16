from flask_wtf import Form
from wtforms import StringField, SelectField,TextField
from wtforms.validators import DataRequired, Required, EqualTo

# Cadastra Processo
class CadastrarProcessoForm(Form):
    processo_tipo = StringField('Tipo Processo', validators=[DataRequired('Tipo do Processo é obrigatório')])
    processo_descricao = TextField('Descricao Processo', validators=[DataRequired('Descricao do Processo é obrigatório')])
    processo_usuario = SelectField('Usuário Processo', validators=[DataRequired('Usuário do Processo é obrigatório.')], coerce=int)
