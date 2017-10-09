from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField, FieldList, RadioField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from werkzeug import secure_filename
from flask_wtf.file import FileRequired

# Cadastra Funcionario
class CadastrarFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    funcionario_setor_id = SelectField('Setor', coerce=int)
    file = FileField("Entre com uma imagem", validators=[FileRequired()])
