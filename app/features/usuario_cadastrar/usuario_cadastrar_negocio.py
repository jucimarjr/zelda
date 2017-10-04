from usuario_cadastrar_form import CadastrarUsuarioForm
from flash_errors_negocio import FlashErrorsNegocio
from ...usuario2.usuario_interface import UsuarioInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

class UsuarioCadastrarNegocio:
    
    def exibir():
        if(session['user_login'] == ""):
            return redirect(url_for('index'))

        form = CadastrarUsuarioForm()
        if form.validate_on_submit():
            usuario = Usuario(login=form.usuario_login.data, senha=Criptografador.gerar_hash(form.usuario_senha.data, ''), admin=form.usuario_admin.data - 1)

            db.cadastra_usuario(usuario)
            return redirect(url_for('usuario_listar'))
        else:
            flash_errors(form)
            return render_template('usuario_criar.html', form=form)