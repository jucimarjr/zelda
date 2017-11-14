from flask import render_template, flash, redirect, url_for, request
from .processo_editar_form import EditarProcessoForm
from ..features.Equipe_13.tables.processo.processo_modelo import Processo
from ...utils.flash_errors import flash_errors
from ...cursor import db

class ProcessoEditarNegocio:    
    def exibir(processo_id):        
        form = EditarProcessoForm()

        processo = Processo(processo_id = processo_id)

        if request.method == 'GET':

            if processo.get_id() is not None:
                form.processo_descricao.data = processo.descricao
                form.processo_id.data = processo.get_id()
            else:
                return redirect(url_for('processo_listar_13'))

        elif form.validate_on_submit():
            processo.descricao = form.processo_descricao.data
            processo.salva()

            return redirect(url_for('processo_listar_13'))
        else:
            flash_errors(form)

        return render_template('processo_editar_13.html', form=form)
