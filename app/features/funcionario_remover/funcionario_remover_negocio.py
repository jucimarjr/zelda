from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from ...funcionario.funcionario_interface import FuncionarioInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL
from ...authentication import verifica_sessao

class FuncionarioRemoverNegocio:

    def exibir(func_id, db):
        if verifica_sessao() == True:
            return redirect(url_for('login'))

        funcionario = db.get_funcionario(func_id)
        if funcionario is None:
            return redirect(url_for('funcionario_listar'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            db.deleta_funcionario(func_id)
        else:
            return render_template('funcionario_desativar.html', funcionario=funcionario)
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra
    página de listagem"""
        return redirect(url_for('funcionario_listar'))