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

    def exibir(db):
        if verifica_sessao() == True:
            return redirect(url_for('login'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':

            ids = request.form.getlist("ids[]")
            if request.form['origem'] == 'propria':
                # Percorre a lista de ids do FieldList
                for item in ids:
                    # do qual pegamos o primeiro e único elemento
                    db.deleta_funcionario(item)
            # Se o form é inválido e a página foi acessada por POST
            else:
                funcionarios = []
                if ids is not None and len(ids) > 0:
                    # Lista os dados de cada funcionário na lista de ids[]
                    for func_id in ids:
                        funcionario = db.get_funcionario(func_id)
                        if funcionario is not None:
                            funcionarios.append(funcionario)
                    return render_template('funcionario_desativar.html', form=request.form, funcionarios=funcionarios)
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra
    página de listagem"""
        return redirect(url_for('funcionario_listar'))