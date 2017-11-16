from flask_wtf import Form
from wtforms import HiddenField
from wtforms.validators import DataRequired

# Remover Setor
class RemoverDocumentoForm(Form):
    documento_id = HiddenField('ID Setor', validators=[DataRequired('O ID do Documento não pode ser indefinido')])
