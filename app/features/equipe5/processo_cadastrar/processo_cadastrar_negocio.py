from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import CadastrarProcessoForm
from ...utils.flash_errors import flash_errors
from ...tables.equipe5.processo_modelo import Processo

class ProcessoCadastrarNegocio:
    def exibir():
        form = CadastrarProcessoForm()

        if form.validate_on_submit():
            processo = Processo()
            processo.desc = form.processo_desc.data
            processo.tipo = form.processo_tipo.data
            processo.salva()

            return redirect(url_for('processo_listar_5'))
        else:
            flash_errors(form)

        return render_template('processo_criar_5.html', form=form)
