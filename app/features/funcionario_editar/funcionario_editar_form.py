from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField, FieldList, RadioField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired

# Atualiza Funcionario
class EditarFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    lotacao_id = HiddenField('ID Lotação', validators=[])
    setor_id = SelectField('Setor', coerce=int)
    funcionario_id = HiddenField('ID Funcionário', validators=[DataRequired('O ID do Funcionário não pode ser indefinido')])