from .processo_editar_form import EditarProcessoForm
from ....tables.equipe10.processo.processo_modelo import Processo
from ....utils.flash_errors import flash_errors
from ....utils.zelda_modelo import ZeldaModelo
from flask import render_template, flash, redirect, url_for

class ProcessoEditarNegocio:

    def exibir(processo_id):
        form = EditarProcessoForm()

        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar'))

        documentos = ZeldaModelo.lista_documentos()
        form.documentos_ids.choices = [(d.get_id(), d.nome) for d in documentos]

        if form.validate_on_submit():
            processo.tipo = form.processo_tipo.data
            processo.desc = form.processo_desc.data
            processo.salva()

            processo.altera_documentos(form.documentos_ids.data)
            return redirect(url_for('processo_listar'))
        else:
            flash_errors(form)

        form.processo_tipo.data = processo.tipo
        form.processo_desc.data = processo.desc
        return render_template('processo_editar.html', form=form)