from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Cadastra Funcionario
class CadastrarFuncionalidadeForm(Form):
    funcionalidade_nome = StringField('Nome Funcionalidade', validators=[DataRequired('Nome da Funcionalidade é obrigatória')])
    funcionalidade_codigo = StringField('Codigo Funcionalidade', validators=[DataRequired('Código da Funcionalidade é obrigatório')])
    funcionalidade_desc = StringField('Descricao Funcionalidade')
    file = FileField('Foto do Funcionário', validators=[])
