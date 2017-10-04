from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from login_form import LoginForm
from ..Criptografador import Criptografador
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

class LoginNegocio:

    def exibir():
        form = LoginForm()
        if form.validate_on_submit():
            session['user_login'] = form.login.data
            senha = form.senha.data
            senhaHash = Criptografador.gerar_hash(senha, '')

            ans = db.verifica_login(login=form.login.data, senha=senhaHash)
            if ans:
                if (not db.verifica_logado(login=form.login.data)):
                    db.set_logado_true(login=form.login.data)
                    if (db.verifica_admin(login=form.login.data)):
                        return redirect(url_for('admin_home'))
                    return redirect(url_for('index'))
                flash("Usuario já logado!")

            else:
                flash("Nome de usuário ou senha incorretos")
        else:
            FlashErrorsNegocio.flash_errors(form)

        return render_template('login.html', form=form)