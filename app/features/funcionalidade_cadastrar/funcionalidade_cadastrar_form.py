from flask_wtf import Form
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired

class CadastrarFuncionalidadeForm(Form):
    funcionalidade_nome = StringField('Nome', validators=[DataRequired('Nome da Funcionalidade é obrigatória')])
    funcionalidade_desc = TextAreaField('Descrição')
    funcionalidade_sistema = SelectField('Sistema', validators=[DataRequired('A funcionalidade deve pertencer a um sistema')], coerce=int)
    funcionalidade_caminho = StringField('Caminho', validators=[DataRequired('A funcionalidade precisa de um caminho para ser acessada')])
    funcionalidade_imagem = FileField('Imagem')