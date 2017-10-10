from flask_wtf import Form
from wtforms import StringField, SelectField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Atualiza Funcionario
class EditarFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    lotacao_id = HiddenField('ID Lotação', validators=[])
    setor_id = SelectField('Setor', coerce=int)
    funcionario_id = HiddenField('ID Funcionário', validators=[DataRequired('O ID do Funcionário não pode ser indefinido')])
    file = FileField("Edite a imagem",validators=[FileRequired()])
