from setor_editar_form import EditarSetorForm
from ...setor2.setor_modelo import Setor
from flash_errors_negocio import FlashErrorsNegocio
from ...setor2.setor_interface import SetorInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

class SetorEditarNegocio:    
    def exibir(setor_id):
        form = EditarSetorForm()

        setor = Setor()

        if request.method == 'GET':

            setor = db.get_setor(setor_id)

            if setor is not None:
                form.setor_nome.data = setor.nome
                form.setor_id.data = setor.id
            else:
                return redirect(url_for('setor_listar'))

        elif form.validate_on_submit():
            setor.nome = form.setor_nome.data
            setor.id = form.setor_id.data

            db.edita_setor(setor)

            return redirect(url_for('setor_listar'))
        else:
            flash_errors(form)

        return render_template('setor_editar.html', form=form)