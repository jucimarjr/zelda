from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField, FieldList, RadioField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired

# Cadastra Documento
class DocumentoCadastrarForm(Form):
    documento_descricao = StringField('Descrição documento', validators=[DataRequired('Descrição do documento é obrigatório')])
    documento_tipo = StringField('Tipo documento', validators=[DataRequired('Tipo do documento é obrigatório')])
    documento_processo = SelectField('Processo documento', validators=[DataRequired('O documento deve estar vinculado a um processo')])