from flask import render_template, flash, redirect, url_for, request
from .funcionalidade_remover_form import RemoverFuncionalidadeForm
from ...utils.flash_errors import flash_errors
from ...tables.funcionalidade.funcionalidade_modelo import Funcionalidade

class FuncionalidadeRemoverNegocio:

    def exibir(funcionalidade_id):
        funcionalidade = Funcionalidade(funcionalidade_id)
        if funcionalidade.get_id() is None:
            return redirect(url_for('funcionalidade_listar'))

        if request.method == 'POST':
            funcionalidade.desativa()
        else:
            return render_template('funcionalidade_desativar.html', funcionalidade = funcionalidade)
        
        return redirect(url_for('funcionalidade_listar'))
