from flask import render_template, flash, redirect, url_for, request
from .processo_remover_form import RemoverProcessoForm
from .....utils.flash_errors import flash_errors
from .....tables.equipe_11.processo.processo_modelo import Processo

class ProcessoRemoverNegocio:

    def exibir(processo_id):
        processo_aux = eval(processo_id)
        processo = Processo(processo_aux)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar'))

        if request.method == 'POST':
            processo.desativa()
        else:
            return render_template('processo_desativar_11.html', processo = processo)

        return redirect(url_for('processo_listar'))
