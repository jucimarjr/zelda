
from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import ProcessoCadastrarForm
from .....cursor import db
from .....utils.flash_errors import flash_errors
from ...tables.processo.processo_modelo import Processo
from .....utils.zelda_modelo_13 import ProcessoModelo


class ProcessoCadastrarNegocio:

    def exibir():

        form = ProcessoCadastrarForm()

        if form.validate_on_submit():

            processo = Processo()

            processo.tipo = form.processo_tipo.data
            processo.descricao = form.processo_descricao.data
            processo.salva()

            return redirect(url_for('processo_listar_2'))

        else:
            flash_errors(form)

        return render_template('processo_criar_13.html', form=form)
