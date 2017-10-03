from usuario_editar_form import EditarUsuarioForm
from flash_errors_negocio import FlashErrorsNegocio
from ...usuario2.usuario_interface import UsuarioInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

class UsuarioEditarNegocio:
    def exibir(user_id):
        if(session['user_login'] == ""):
            return redirect(url_for('index'))

        form = EditarUsuarioForm()

        usuario = Usuario()

        if form.validate_on_submit():
            usuario.login = form.usuario_login.data
            usuario.id = form.usuario_id.data
            usuario.senha = Criptografador.gerar_hash(form.usuario_senha.data, '')
            usuario.admin = form.usuario_admin.data - 1

            db.edita_usuario(usuario)

            return redirect(url_for('usuario_listar'))
        else:

            usuario = db.get_usuario(user_id)

            if usuario is not None:
                form.usuario_admin.default = int(usuario.admin + 1)
                form.process()

                form.usuario_login.data = usuario.login
                form.usuario_id.data = user_id

            else:
                return redirect(url_for('usuario_listar'))

            flash_errors(form)

        return render_template('usuario_editar.html', form=form)