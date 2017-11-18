from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField, FieldList, RadioField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired

# Cadastra Processo
class CadastrarProcessoForm(Form):
    processo_descricao = StringField('Descrição processo', validators=[DataRequired('Descrição do processo é obrigatório')])
    processo_tipo = StringField('Processo Tipo', validators=[DataRequired('Tipo do Processo é obrigatório')])
