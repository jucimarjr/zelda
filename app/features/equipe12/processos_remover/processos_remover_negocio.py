from flask import render_template, flash, redirect, url_for, request
from .processos_remover_form import ProcessoRemoverForm
from ....tables.equipe_12.processos.processos_modelo import Processo12
from ....utils.flash_errors import flash_errors
from ....cursor import db
from ....utils.processos_modelo_12 import ProcessaModelo

class ProcessoRemoverNegocio:

    def exibir(processo_id):
        processo = Processo12(processo_id)
        if processo.get_id_12()is None:
            return redirect(url_for('processos_listar_12'))

        if request.method == 'POST':
            processo.desativa()
        else:
            return render_template('processos_remover_12.html',processo=processo)

        return redirect(url_for('processos_listar_12'))
