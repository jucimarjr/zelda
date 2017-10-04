from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from .setor_remover_form import RemoverSetorForm
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from ...setor.setor_interface import SetorInterface
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

class SetorRemoverNegocio:
    def exibir(db):
        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':

            ids = request.form.getlist("ids[]")

            if request.form['origem'] == 'propria':

                for item in ids:
                    # do qual pegamos o primeiro e único elemento
                    db.deleta_setor(item)

            # Se o form é inválido e a página foi acessada por POST
            else:
                setores = []

                if ids is not None and len(ids) > 0:

                    # Lista os dados de cada setor na lista de ids[]
                    for set_id in ids:
                        setor = db.get_setor(set_id)

                        if setor is not None:
                            setores.append(setor)

                    return render_template('setor_desativar.html', form=request.form, setores=setores)

        """Se o método foi GET ou o form deu erro de submissão, redireciona pra
        página de listagem"""
        return redirect(url_for('setor_listar'))
