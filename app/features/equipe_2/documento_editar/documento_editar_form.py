from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

# Edita documento
class EditarDocumentoForm(Form):
    documento_nome = StringField('Nome documento', validators=[DataRequired('Nome do documento é obrigatório')])
    # Hidden Field é muito usado em CRUDs para passar dados do model entre requisições, nesse caso, a tela de
    # atualizar deve ter um id do elemento a ser alterado sendo transmitido no formulário de maneira escondida
    documento_id = HiddenField('ID documento', validators=[DataRequired('O ID do documento não pode ser indefinido')])
