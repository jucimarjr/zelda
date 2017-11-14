from flask import render_template, redirect, url_for, request
from ...tables.processo.processo_modelo import Processo

class ProcessoRemoverNegocio:
    def exibir(processo_id):
        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('equipe1_processo_listar'))

        if request.method == 'POST':
            processo.remove()
            return redirect(url_for('equipe1_processo_listar'))

        return render_template('equipe1_processo_remover.html', processo = processo)