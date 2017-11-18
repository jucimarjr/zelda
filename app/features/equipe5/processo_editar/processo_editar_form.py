from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

# Edita Processo
class EditarProcessoForm(Form):
    processo_descricao = StringField('Descrição processo', validators=[DataRequired('Descrição do processo é obrigatório')])
    processo_tipo = StringField('Tipo processo', validators=[DataRequired('Tipo do processo é obrigatório')])
    # Hidden Field é muito usado em CRUDs para passar dados do model entre requisições, nesse caso, a tela de
    # atualizar deve ter um id do elemento a ser alterado sendo transmitido no formulário de maneira escondida
    processo_id = HiddenField('ID processo', validators=[DataRequired('O ID do processo não pode ser indefinido')])
