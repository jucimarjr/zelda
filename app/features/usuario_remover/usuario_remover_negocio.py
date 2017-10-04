from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from .usuario_remover_form import RemoverUsuarioForm
from ...usuario.usuario_interface import UsuarioInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from ...authentication import verifica_sessao

class UsuarioRemoverNegocio:
    
    def exibir(db):
        if verifica_sessao() == True:
            return redirect(url_for('login'))

        form = RemoverUsuarioForm()
        if request.method == 'POST':

            ids = request.form.getlist("ids[]")

            if request.form['origem'] == 'propria':

                # Percorre a lista de ids do FieldList
                for item in ids:
                    # do qual pegamos o primeiro e único elemento
                    db.deleta_usuario(item)

            # Se o form é inválido e a página foi acessada por POST
            else:
                usuarios = []

                if ids is not None and len(ids) > 0:

                    # Lista os dados de cada funcionário na lista de ids[]
                    for user_id in ids:
                        usuario = db.get_usuario(user_id)

                        if usuario is not None:
                            usuarios.append(usuario)

                    return render_template('usuario_remover.html', form=request.form, usuarios=usuarios)

        """Se o método foi GET ou o form deu erro de submissão, redireciona pra página de listagem"""
        return redirect(url_for('usuario_listar'))