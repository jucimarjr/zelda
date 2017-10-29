from flask_wtf import Form
from wtforms import HiddenField
from wtforms.validators import DataRequired

# Remover Funcionalidade
class RemoverFuncionalidadeForm(Form):
    funcionalidade_id = HiddenField('ID Funcionalidade', validators=[DataRequired('O ID da Funcionalidade não pode ser indefinido')])