from flask import render_template, flash, redirect, url_for, request
from .processo_editar_form import EditarProcessoForm
from ...tables.equipe5.processo_modelo import Processo
from ...utils.flash_errors import flash_errors
from ...cursor import db

class ProcessoEditarNegocio:    
    def exibir(processo_id):        
        form = EditarProcessoForm()

        processo = Processo(processo_id = processo_id)

        if request.method == 'GET':

            if processo.get_id() is not None:
                form.processo_desc.data = processo.desc
                form.processo_tipo.data = processo.tipo
                form.processo_id.data = processo.get_id()
            else:
                return redirect(url_for('processo_listar_5'))

        elif form.validate_on_submit():
            processo.desc = form.processo_desc.data
            processo.tipo = form.processo_desc.data
            processo.salva()

            return redirect(url_for('processo_listar_5'))
        else:
            flash_errors(form)

        return render_template('processo_editar_5.html', form=form)
