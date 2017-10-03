from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField, FieldList, RadioField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired


# Cadastra Usuario
class CadastrarUsuarioForm(Form):
    usuario_login = StringField('Login Usuario', validators=[DataRequired('Login do Usuario é obrigatório')])
    usuario_senha = PasswordField('Senha', validators=[DataRequired('Senha do Usuario é obrigatório')])
    usuario_admin = RadioField('Tipo do Usuário', validators=[DataRequired('Tipo do Usuário é obrigatório')], choices=[(1, 'Administrador'), (2, 'Usuário Comum')], coerce=int)

