from .processo_cadastrar_form import CadastrarProcessoForm
from ....tables.equipe10.processo.processo_modelo import Processo
from ....utils.flash_errors import flash_errors
from ....utils.zelda_modelo import ZeldaModelo
from flask import render_template, flash, redirect, url_for

class ProcessoCadastrarNegocio:

    def exibir():
        form = CadastrarProcessoForm()

        documentos = ZeldaModelo.lista_documentos()
        form.documentos_ids.choices = [(d.get_id(), d.tipo) for d in documentos]

        if form.validate_on_submit():

            processo = Processo()
            processo.tipo = form.processo_tipo.data
            processo.desc = form.processo_desc.data
            processo.salva()
            processo.altera_documentos(form.documentos_ids.data)

            return redirect(url_for('processo_listar'))
        else:
            flash_errors(form)

        return render_template('processo_criar.html', form=form)