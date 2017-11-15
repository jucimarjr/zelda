from flask import render_template, flash, redirect, url_for, request
from ....tables.equipe_12.processos.processos_modelo import Processo12
from .processos_editar_form import EditarProcessoForm
from ..processos_cadastrar.processos_cadastrar_form import CadastrarProcessoForm

from ....utils.flash_errors import flash_errors
from ....utils.processos_modelo_12 import ProcessaModelo
from ....utils.files import flash_errors_extensao

class ProcessoEditarNegocio():
    def exibir(processo_id):

        form = EditarProcessoForm()
        processo = Processo12(processo_id = processo_id)

        if processo.get_id_12() is None:
            return redirect(url_for('processos_listar_12'))

        if form.validate_on_submit():
            processo.tipo = form.processo_tipo.data
            processo.desc = form.processo_desc.data
            processo.salva()
            return redirect(url_for('processos_listar_12'))
        else:
            flash_errors(form)

        form.processo_tipo.data = processo.tipo
        form.processo_desc.data = processo.desc
        return render_template('processos_editar_12.html',form=form)
