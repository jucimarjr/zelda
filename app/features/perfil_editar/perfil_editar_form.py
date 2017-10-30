from flask_wtf import Form
from wtforms import StringField, SelectMultipleField
from wtforms.validators import DataRequired


class EditarPerfilForm(Form):
    perfil_nome = StringField('Perfil', validators=[DataRequired('Nome do Perfil é obrigatório')])
    funcionalidades_ids = SelectMultipleField('Funcionalidades', validators=[DataRequired('Funcionalidade é obrigatória')], choices=[(1, 'Menu de Funcionários'), (2, 'Menu de Setores'), (3, 'Menu de Usuário'), (4, 'Menu de Sistemas'), (5, 'Menu de Funcionalidades'), (6, 'Menu de Perfis')], coerce=int)