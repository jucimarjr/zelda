from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from ...usuario.usuario_interface import UsuarioInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from ...authentication import verifica_sessao

class UsuarioRemoverNegocio:
    
    def exibir(user_id, db):
        if verifica_sessao() == True:
            return redirect(url_for('login'))

        usuario = db.get_usuario(user_id)
        if usuario is None:
            return redirect(url_for('usuario_listar'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            db.deleta_usuario(user_id)
        else:
            return render_template('usuario_remover.html', usuario=usuario)
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra
    página de listagem"""
        return redirect(url_for('usuario_listar'))
