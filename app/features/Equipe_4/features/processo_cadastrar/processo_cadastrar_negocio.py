from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import CadastrarProcessoForm
from app.cursor import db
from app.utils.flash_errors import flash_errors
from app.tables.equipe4.tables.processo.processo_modelo import Processo
from app.utils.zelda_modelo_4 import ZeldaModelo


class ProcessoCadastrarNegocio:

    def exibir():

        form = CadastrarProcessoForm()

        if form.validate_on_submit():

            processo = Processo()

            processo.tipo = form.processo_tipo.data
            processo.desc = form.processo_desc.data
            processo.salva()

            return redirect(url_for('processo_listar'))

        else:
            flash_errors(form)

        return render_template('equipe4_processo_criar.html', form=form)
