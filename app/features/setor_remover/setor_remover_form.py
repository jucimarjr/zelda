from flask_wtf import Form
from wtforms import HiddenField
from wtforms.validators import DataRequired

# Remover Setor
class RemoverSetorForm(Form):
    setor_id = HiddenField('ID Setor', validators=[DataRequired('O ID do Setor não pode ser indefinido')])