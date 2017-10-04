from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from .classes import Criptografador
from flask_mysqldb import MySQL
from .db_interface import Zelda
from .authentication import *
from .features.criptografador.criptografador_negocio import Criptografador

from .cursor import db
from app import app


from .features.login.login_form import LoginForm

# Index
@app.route('/')
@app.route('/index')
def index():
    if(verifica_sessao()==True):
        return redirect(url_for('login'))

    usuario = retorna_usuario(db)
    return render_template('usuario_home.html', usuario=usuario)


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user_login = form.login.data
        user_senha = form.senha.data
        inicia_sessao(user_login = user_login)
        if (autentica(user_senha, db)):
            if (is_logado(db)):
                set_logado(True, db)
                if (is_admin(db)):
                    return redirect(url_for('admin_home'))
                return redirect(url_for('index'))
            flash("Usuario já logado!")
            encerra_sessao()
        flash("Nome de usuário ou senha incorretos")
        encerra_sessao()
    else:
        flash_errors(form)

    return render_template('login.html', form=form)


@app.route('/logout/')
def logout():
    encerra_sessao()
    return redirect(url_for('login'))


@app.route('/admin')
def admin_home():
    if(verifica_sessao()==True):
        return redirect(url_for('login'))

    usuario = retorna_usuario(db)
    return render_template('admin_home.html', usuario = usuario)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error))
