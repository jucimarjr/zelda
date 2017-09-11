from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import FlaskForm
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators,BooleanField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired

class LoginForms(FlaskForm):
	usuario = StringField('Email',validators=[DataRequired()])
	senha = PasswordField('Senha', validators=[DataRequired()])

#Cadastra Funcionario
class CadastraFuncionarioForms(Form):
    funcionario_id = StringField('ID', [validators.Length(min=1, max=12)])
    funcionario_nome = StringField('Name', [validators.Length(min=1, max=50)])
    funcionario_login = StringField('Username', [validators.Length(min=4, max=50)])
    funcionario_senha = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    funcionario_email = StringField('Email', [validators.Length(min=6, max=50)])
    funcionario_status = StringField('Status (-1, 0, 1)', [validators.Length(min=1 , max=1)])
    funcionario_matricula = StringField('Matrícula', [validators.Length(min=6, max=12)])
    funcionario_ultimo_acesso = StringField('Ultimo acesso', [validators.Length(min=10, max=10)])
    funcionario_enviados = StringField('Enviados', [validators.Length(min=1, max=100)])
    funcionario_recebidos = StringField('Recebidos', [validators.Length(min=1, max=100)])
    funcionario_telefone = StringField('Telefone', [validators.Length(min=9, max=9)])
    funcionario_unidade = StringField('Unidade', [validators.Length(min=2, max=100)])

#Cadastra Setor
class CadastraSetorForms(Form):
        setor_id = StringField('ID',[validators.Length(min=1, max=12)])
        setor_nome = StringField('Name', [validators.Length(min=1, max=50)])
        setor_status = StringField('Satatus (-1, 0, 1)',[validators.Length(min=1 , max=1)])

