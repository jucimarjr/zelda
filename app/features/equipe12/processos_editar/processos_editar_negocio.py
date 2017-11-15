from flask import render_template, flash, redirect, url_for, request
from ....tables.equipe_12.processos.processos_modelo import Processo12
from .processos_editar_form import EditarProcessoForm
from ..processos_cadastrar.processos_cadastrar_form import CadastrarProcessoForm

from ....utils.flash_errors import flash_errors
from ....utils.processos_modelo_12 import ProcessaModelo
from ....utils.files import flash_errors_extensao

class ProcessoEditarNegocio():
    def exibir(funcionalidade_id):

        form = EditarProcessoForm()
        processo = Processo(processo_id = processo_id)

        if request.method == 'GET':

            if processo.get_id() is not None:
                form.processo_tipo.data = processo_tipo
                form.processo_desc.data = processo_desc
            else:
                return redirect(url_for('processo_listar'))

        if form.validate_on_submit():
            form.processo_tipo.data = processo_tipo
            form.processo_desc.data = processo_desc
            processo.salva()
        else:
            flash_errors(form)

        return render_template('processo_editar.html', form=form)
