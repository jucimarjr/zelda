from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

# Edita Processo
class EditarProcessoForm(Form):
    processo_nome = TextAreaField('Descrição')
    processo_tipo = StringField('Nome Setor', validators=[DataRequired('Nome do Setor é obrigatório')])
    # Hidden Field é muito usado em CRUDs para passar dados do model entre requisições, nesse caso, a tela de
    # atualizar deve ter um id do elemento a ser alterado sendo transmitido no formulário de maneira escondida
    processo_id = HiddenField('ID Processo', validators=[DataRequired('O ID do Processo não pode ser indefinido')])
