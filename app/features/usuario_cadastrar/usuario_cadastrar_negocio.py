from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from .usuario_cadastrar_form import CadastrarUsuarioForm
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from ...usuario.usuario_interface import UsuarioInterface
from ...usuario.usuario_modelo import Usuario
from ..criptografador.criptografador_negocio import Criptografador
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

class UsuarioCadastrarNegocio:
    
    def exibir(db):
        if(session['user_login'] == ""):
            return redirect(url_for('index'))

        form = CadastrarUsuarioForm()
        if form.validate_on_submit():
            usuario = Usuario(login=form.usuario_login.data, senha=Criptografador.gerar_hash(form.usuario_senha.data, ''), admin=form.usuario_admin.data - 1)

            db.cadastra_usuario(usuario)
            return redirect(url_for('usuario_listar'))
        else:
            FlashErrorsNegocio.flash_errors(form)
            return render_template('usuario_criar.html', form=form)