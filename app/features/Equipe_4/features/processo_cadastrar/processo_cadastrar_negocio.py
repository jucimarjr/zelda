from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import CadastrarProcessoForm
from ....cursor import db
from ....utils.flash_errors import flash_errors
from ....features.Equipe_4.processo.processo_modelo import Processo
from ....utils.zelda_modelo_4 import ZeldaModelo

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
