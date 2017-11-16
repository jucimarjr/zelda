from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Required



class EditarProcessoForm(Form):
    processo_tipo = StringField('Tipo do Processo', validators=[DataRequired('Tipo do Processo é obrigatório.')])
    processo_descricao = StringField('Descrição do Processo', validators=[DataRequired('Descrição do Processo é obrigatório.')])


