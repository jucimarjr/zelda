from flask import render_template, redirect, url_for, request
from ..features.Equipe_13.tables.processo.processo_modelo import Processo

class ProcessoRemoverNegocio:
    def exibir(processo_id):
        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('equipe13_processo_listar'))

        if request.method == 'POST':
            processo.remove()
            return redirect(url_for('equipe13_processo_listar'))

        return render_template('equipe13_processo_remover.html', processo = processo)
