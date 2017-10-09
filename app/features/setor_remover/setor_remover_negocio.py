from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from .setor_remover_form import RemoverSetorForm
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from ...setor.setor_interface import SetorInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL
from ...authentication import verifica_sessao

class SetorRemoverNegocio:

    def exibir(setor_id, db):
        if verifica_sessao() == True:
            return redirect(url_for('login'))

        setor = db.get_funcionario(setor_id)
        if setor is None:
            return redirect(url_for('setor_listar'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            db.deleta_setor(setor_id)
        else:
            return render_template('setor_desativar.html', setor=setor)
        
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra página de listagem"""
        return redirect(url_for('setor_listar'))
