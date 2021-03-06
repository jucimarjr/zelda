from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class ProcessoCadastrarForm(Form):
    descricao = StringField('Descrição', validators=[DataRequired('Descrição é obrigatória')])
    tipo = SelectField('Tipo do Processo', validators=[DataRequired('Tipo do processo é obrigatório')], coerce = int)
    usuario = SelectField('Usuário', validators=[DataRequired('Usuário é obrigatório')], coerce = int)