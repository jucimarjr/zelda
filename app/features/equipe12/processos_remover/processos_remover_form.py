from flask_wtf import Form
from wtforms import HiddenField
from wtforms.validators import DataRequired

# Remover Processo
class ProcessoRemoverForm(Form):
    processo_id = HiddenField('ID Setor', validators=[DataRequired('O ID do Processo não pode ser indefinido')])
