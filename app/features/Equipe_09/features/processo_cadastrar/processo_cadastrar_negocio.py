from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import CadastrarProcessoForm
from ...utils.flash_errors import flash_errors
from ...tables.processo.processo_modelo import Processo
from ...tables.documento.documento_modelo import Documento

class ProcessoCadastrarNegocio:
    def exibir():
        form = CadastrarProcessoForm()

        if form.validate_on_submit():
            processo = Processo()
            processo.tipo = form.processo_tipo.data
            processo.descricao = form.processo_descricao.data
            processo.salva()

            return redirect(url_for('processo_listar'))
        else:
            flash_errors(form)

        return render_template('processo_criar.html', form=form)
