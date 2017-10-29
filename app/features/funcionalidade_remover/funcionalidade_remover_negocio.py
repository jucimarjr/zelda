from flask import render_template, flash, redirect, url_for, request
from .funcionalidade_remover_form import RemoverFuncionalidadeForm
from ...utils.flash_errors import flash_errors
from ...cursor import db
from ...tables.funcionalidade.funcionalidade_modelo import Funcionalidade

class FuncionalidadeRemoverNegocio:

    def exibir(funcionalidade_id):
        funcionalidade = db.get_funcionalidade(funcionalidade_id)

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            funcionalidade.funcionalidade_situacao = 1
        else:
            return render_template('funcionalidade_desativar.html', funcionalidade=funcionalidade)
        
        return redirect(url_for('funcionalidade_listar'))
