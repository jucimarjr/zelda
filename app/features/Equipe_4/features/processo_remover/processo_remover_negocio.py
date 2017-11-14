from flask import Flask, render_template, flash, redirect, url_for, request
from ....utils.flash_errors import flash_errors
<<<<<<< HEAD:app/features/Equipe_4/features/processo_remover/processo_remover_negocio.py
from ....features.Equipe_4.processo.processo_modelo import Processo
=======
from ....tables.processo.processo_modelo import Processo
>>>>>>> 2d01658080d0fc3a8428dc3595386d3da0c04b94:app/features/Equipe_4/processo_remover_negocio.py

class ProcessoRemoverNegocio:

    def exibir(processo_id):
        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar'))

        if request.method == 'POST':
            processo.deleta()
            return redirect(url_for('processo_listar'))

        return render_template('equipe4_processo_remover.html', processo = processo)
