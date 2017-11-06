from .sistema_cadastrar_form import CadastrarSistemaForm
from ...tables.sistema.sistema_modelo import Sistema
from ...utils.flash_errors import flash_errors
from ...utils.zelda_modelo import ZeldaModelo

from flask import render_template, flash, redirect, url_for

class SistemaCadastrarNegocio:

    def exibir():
        form = CadastrarSistemaForm()

        if form.validate_on_submit():

            sistema = Sistema()
            sistema.nome = form.sistema_nome.data
            sistema.desc = form.sistema_desc.data
            sistema.prefixo = form.sistema_prefixo.data
            sistema.status = form.sistema_status.data


            sistema.salva()
            return redirect(url_for('sistema_listar'))
        else:
            flash_errors(form)

        return render_template('sistema_criar.html', form=form)
