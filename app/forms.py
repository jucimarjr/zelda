from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField, FieldList, RadioField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired


# Cadastra Login
class LoginForm(Form):
    login = StringField('Nome de Usuário', validators=[DataRequired('Nome de Usuário é obrigatório')])
    senha = PasswordField('Senha', validators=[DataRequired('Senha é obrigatório')])


# Cadastra Funcionario
class CadastraFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    funcionario_setor_id = SelectField('Setor', coerce=int)


# Cadastra Usuario
class CadastraUsuarioForm(Form):
    usuario_login = StringField('Login Usuario', validators=[DataRequired('Login do Usuario é obrigatório')])
    usuario_senha = PasswordField('Senha', validators=[DataRequired('Senha do Usuario é obrigatório')])
    usuario_admin = RadioField('Tipo do Usuário', validators=[DataRequired('Tipo do Usuário é obrigatório')], choices=[(1, 'Administrador'), (2, 'Usuário Comum')], coerce=int)


# Cadastra Setor
class CadastraSetorForm(Form):
    setor_nome = StringField('Nome Setor', validators=[DataRequired('Nome do Setor é obrigatório')])


# Atualiza Setor
class AtualizaSetorForm(Form):
    setor_nome = StringField('Nome Setor', validators=[DataRequired('Nome do Setor é obrigatório')])
    # Hidden Field é muito usado em CRUDs para passar dados do model entre requisições, nesse caso, a tela de
    # atualizar deve ter um id do elemento a ser alterado sendo transmitido no formulário de maneira escondida
    setor_id = HiddenField('ID Setor', validators=[DataRequired('O ID do Setor não pode ser indefinido')])


# Atualiza Funcionario
class AtualizaFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    lotacao_id = HiddenField('ID Lotação', validators=[])
    setor_id = SelectField('Setor', coerce=int)
    funcionario_id = HiddenField('ID Funcionário', validators=[DataRequired('O ID do Funcionário não pode ser indefinido')])


# Atualiza Usuário
class AtualizaUsuarioForm(Form):
    usuario_login = StringField('Login do Usuário', validators=[DataRequired('Login do Usuário é obrigatório')])
    usuario_admin = RadioField('Tipo do Usuário', validators=[DataRequired('Tipo do Usuário é obrigatório')], choices=[(1, 'Administrador'), (2, 'Usuário Comum')], coerce=int)
    usuario_id = HiddenField('ID Usuário', validators=[DataRequired('O ID do Usuário não pode ser indefinido')])
    usuario_senha = PasswordField('Senha do Usuário', validators=[DataRequired('A senha do Usuário é obrigatória')])


# Remover Funcionário
class RemoveFuncionarioForm(Form):
    # Implementa um campo em forma de lista, cujos elementos serão inputs do tipo HiddenField
    funcionarios_ids = FieldList(HiddenField('IDs dos Funcionários', validators=[DataRequired('Os IDs da lista não podem ser indefinidos')]), validators=[DataRequired('A lista de IDs não pode ser indefinida')])


# Remover Setor
class RemoveSetorForm(Form):
    setor_id = HiddenField('ID Setor', validators=[DataRequired('O ID do Setor não pode ser indefinido')])
    
#Remover Usuário
class RemoveUsuarioForm(Form):
    # Implementa um campo em forma de lista, cujos elementos serão inputs do tipo HiddenField
    usuarios_ids = FieldList(HiddenField('IDs dos Usuários', validators=[DataRequired('Os IDs da lista não podem ser indefinidos')]), validators=[DataRequired('A lista de IDs não pode ser indefinida')])

