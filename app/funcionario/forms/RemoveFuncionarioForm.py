from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SelectField, HiddenField, FieldList, RadioField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired

# Remover Funcionário
class RemoveFuncionarioForm(Form):
    # Implementa um campo em forma de lista, cujos elementos serão inputs do tipo HiddenField
    funcionarios_ids = FieldList(HiddenField('IDs dos Funcionários', validators=[DataRequired('Os IDs da lista não podem ser indefinidos')]), validators=[DataRequired('A lista de IDs não pode ser indefinida')])