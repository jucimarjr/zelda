from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

# Edita Setor
class EditarSetorForm(Form):
    setor_nome = StringField('Nome Setor', validators=[DataRequired('Nome do Setor é obrigatório')])
    # Hidden Field é muito usado em CRUDs para passar dados do model entre requisições, nesse caso, a tela de
    # atualizar deve ter um id do elemento a ser alterado sendo transmitido no formulário de maneira escondida
    setor_id = HiddenField('ID Setor', validators=[DataRequired('O ID do Setor não pode ser indefinido')])