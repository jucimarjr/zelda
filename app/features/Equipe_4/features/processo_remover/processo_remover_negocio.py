from flask import Flask, render_template, flash, redirect, url_for, request
from ....utils.flash_errors import flash_errors
from ....features.Equipe_4.processo.processo_modelo import Processo


class ProcessoRemoverNegocio:

    def exibir(processo_id):
        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar'))

        if request.method == 'POST':
            processo.deleta()
            return redirect(url_for('processo_listar'))

        return render_template('equipe4_processo_remover.html', processo = processo)
