from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField, FieldList, RadioField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired
from .funcionario.forms import *
from .setor.forms import *
from .usuario.forms import *

# Cadastra Login
class LoginForm(Form):
    login = StringField('Nome de Usuário', validators=[DataRequired('Nome de Usuário é obrigatório')])
    senha = PasswordField('Senha', validators=[DataRequired('Senha é obrigatório')])