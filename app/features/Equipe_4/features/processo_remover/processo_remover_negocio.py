from flask import Flask, render_template, flash, redirect, url_for, request
from app.utils.flash_errors import flash_errors
from app.tables.equipe4.tables.processo.processo_modelo import Processo


class ProcessoRemoverNegocio:

    def exibir(processo_id):
        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar_4'))

        if request.method == 'POST':
            processo.deleta()
            return redirect(url_for('processo_listar_4'))

        return render_template('equipe4_processo_remover.html', processo = processo)
