from flask import render_template, redirect, url_for, request
from ...tables.processo.processo_modelo import Processo

class ProcessoRemoverNegocio:
    def exibir(processo_id):
        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar_13'))

        if request.method == 'POST':
            processo.deleta_13()
            return redirect(url_for('processo_listar_13'))

        return render_template('processo_remover_13.html', processo = processo)
