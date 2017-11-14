from flask_wtf import Form
from wtforms import HiddenField
from wtforms.validators import DataRequired

# Remover Processo
class RemoverProcessoForm(Form):
    processo_id = HiddenField('ID Processo', validators=[DataRequired('O ID do Processo não pode ser indefinido')])
