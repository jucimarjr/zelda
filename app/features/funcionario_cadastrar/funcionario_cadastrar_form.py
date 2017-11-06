from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Cadastra Funcionario
class CadastrarFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    funcionario_setor_id = SelectField('Setor', coerce=int)
    #file = FileField('Foto do Funcionário', validators=[])
