from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired

#Cadastra Login
class LoginForm(Form):
    login = StringField('Nome de Usuário', validators=[DataRequired('Nome de Usuário é obrigatório')])
    senha = PasswordField('Senha', validators=[DataRequired('Senha é obrigatório')])

#Cadastra Funcionario
class CadastraFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    funcionario_login = StringField('Login Funcionário', validators=[DataRequired('Login do Funcionário é obrigatório')])
    funcionario_senha = PasswordField('Senha', validators=[DataRequired('Senha é obrigatório')])
    funcionario_setor_id = SelectField ('Setor', coerce=int)

#cadastra Usuario
class CadastraUsuarioForm(Form):
    usuario_login = StringField('Login Usuáiro', validators=[DataRequired('Login do Usuáiro é obrigatório')])
    usuario_senha = PasswordField('Senha', validators=[DataRequired('Senha é obrigatória')])

#Cadastra Setor
class CadastraSetorForm(Form):
    setor_nome = StringField('Nome Setor', validators=[DataRequired('Nome do Setor é obrigatório')])

# Atualiza Setor
class AtualizaSetorForm(Form):
    setor_nome = StringField('Nome Setor', validators=[DataRequired('Nome do Setor é obrigatório')])
    # Hidden Field é muito usado em CRUDs para passar dados do model entre requisições, nesse caso, a tela de
    # atualizar deve ter um id do elemento a ser alterado sendo transmitido no formulário de maneira escondida
    setor_id = HiddenField('ID Setor', validators=[DataRequired('O ID do Setor não pode ser indefinido')])


#Atualiza Funcionario
class AtualizaFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    funcionario_login = StringField('Login Funcionário', validators=[DataRequired('Login do Funcionário é obrigatório')])
    funcionario_senha = PasswordField('Senha', validators=[DataRequired('Senha é obrigatório')])
    funcionario_setor_id = SelectField ('Setor', coerce=int)
    funcionario_id = HiddenField('ID Funcionário', validators=[DataRequired('O ID do Funcionário não pode ser indefinido')])

# Remover Funcionário
class RemoveFuncionarioForm(Form):
    funcionario_id = HiddenField('ID Funcionário', validators=[DataRequired('O ID do Funcionário não pode ser indefinido')])

# Remover Setor
class RemoveSetorForm(Form):
    setor_id = HiddenField('ID Setor', validators=[DataRequired('O ID do Setor não pode ser indefinido')])
