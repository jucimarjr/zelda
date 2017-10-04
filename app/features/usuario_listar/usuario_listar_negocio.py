from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL
from ...authentication import verifica_sessao

class UsuarioListarNegocio:

    def exibir(db):
        if(verifica_sessao() == True):
            return redirect(url_for('login'))

        usuarios = db.get_usuarios()
        return render_template('usuario_listar.html', usuarios=usuarios)