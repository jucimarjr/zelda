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

# Editar Usuário
class EditarUsuarioForm(Form):
    usuario_login = StringField('Login do Usuário', validators=[DataRequired('Login do Usuário é obrigatório')])
    usuario_admin = RadioField('Tipo do Usuário', validators=[DataRequired('Tipo do Usuário é obrigatório')], choices=[(1, 'Administrador'), (2, 'Usuário Comum')], coerce=int)
    usuario_id = HiddenField('ID Usuário', validators=[DataRequired('O ID do Usuário não pode ser indefinido')])
    usuario_senha = PasswordField('Senha do Usuário', validators=[DataRequired('A senha do Usuário é obrigatória')])
    file = FileField("Edite a imagem",validators  = [FileRequired()])
