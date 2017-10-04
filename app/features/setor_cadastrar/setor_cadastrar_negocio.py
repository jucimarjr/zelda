from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from .setor_cadastrar_form import CadastrarSetorForm
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from ...setor.setor_interface import SetorInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

from ...setor.setor_modelo import Setor 

class SetorCadastrarNegocio:
    def exibir(db):
        form = CadastrarSetorForm()

        if form.validate_on_submit():
            setor = Setor(nome=form.setor_nome.data)

            db.cadastra_setor(setor)

            return redirect(url_for('setor_listar'))
        else:
            FlashErrorsNegocio.flash_errors(form)

        return render_template('setor_criar.html', form=form)