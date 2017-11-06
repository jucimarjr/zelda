from flask_wtf import Form
from wtforms import StringField, SelectField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

# Atualiza Funcionario
class EditarFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    setor_id = SelectField('Setor', validators=[DataRequired('O funcionário deve ocupar um setor')], coerce=int)
    #file = FileField("Edite a imagem",validators=[])
