from flask import render_template, flash, redirect, url_for, request
from .....tables.equipe_11.processo.processo_modelo import Processo
from .processo_editar_form import EditarProcessoForm
from ..processo_cadastrar.processo_cadastrar_form import CadastrarProcessoForm
from .....utils.flash_errors import flash_errors
from .....utils.criptografador import Criptografador
from .....utils.zelda_modelo_11 import ZeldaModelo
from .....utils.files import flash_errors_extensao

class ProcessoEditarNegocio:
    def exibir(processo_id):

        form = EditarProcessoForm()
        processo = Processo(processo_id = processo_id)

        if request.method == 'GET':

            if processo.get_id() is not None:
                form.processo_tipo.data = processo.processo_tipo
                form.processo_desc.data = processo.processo_desc

            else:
                return redirect(url_for('processo_listar'))


        if form.validate_on_submit():
            processo.processo_tipo = form.processo_tipo.data
            processo.processo_desc = form.processo_desc.data
            processo.salva()

            return redirect(url_for('processo_listar'))
        else:
            flash_errors(form)

        return render_template('processo_editar_11.html', form=form)
