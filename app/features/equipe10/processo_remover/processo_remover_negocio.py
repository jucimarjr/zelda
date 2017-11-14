from flask import render_template, flash, redirect, url_for, request
from ....utils.flash_errors import flash_errors
from ....tables.equipe10.processo.processo_modelo import Processo


class ProcessoRemoverNegocio:
    def exibir(processo_id):
        processo = Processo(processo_id)

        if processo.get_id() is None:
            return redirect(url_for('processo_listar'))

        if request.method == 'POST':
            processo.desativa()
        else:
            return render_template('processo_desativar.html', processo=processo)

        return redirect(url_for('processo_listar'))
