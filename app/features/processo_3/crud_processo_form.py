from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

# Cadastra Funcionario
class CrudProcesso(Form):
	processo_nome_aluno = StringField('Nome do Aluno', validators=[DataRequired('Nome do Aluno é obrigatório')])
	processo_tipo = StringField('Tipo de Processo', validators=[DataRequired('Tipo de Processo é obrigatório')])
	processo_descricao = StringField('Descrição do Processo', validators=[DataRequired('Descrição do Processo é obrigatório')])
	processo_link = StringField('Link do Processo', validators=[DataRequired('Link do Processo é obrigatório')])
