from flask import render_template, flash, redirect, url_for, request
from .processo_remover_form import RemoverProcessoForm
from ...utils.flash_errors import flash_errors
from ...cursor import db
from ...tables.processo.processo_modelo import Processo

class ProcessoRemoverNegocio:

    def exibir(processo_id):
        processo = (processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            processo.desativa()
        else:
            return render_template('processo_desativar.html', processo=processo)
        
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra página de listagem"""
        return redirect(url_for('processo_listar'))
