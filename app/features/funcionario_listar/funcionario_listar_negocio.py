from ...funcionario2.funcionario_interface import FuncionarioInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

class FuncionarioListarNegocio:
    def exibir():
        if(session['user_login'] == ""):
            return redirect(url_for('index'))
        
        funcionarios = db.get_funcionarios()
        return render_template('funcionario_listar.html', funcionarios=funcionarios)