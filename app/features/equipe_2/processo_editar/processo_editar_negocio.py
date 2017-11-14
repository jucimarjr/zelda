from flask import render_template, flash, redirect, url_for, request
from .processo_editar_form import EditarProcessoForm
from ....tables.equipe_2.processo.processo_modelo import Processo
from ....utils.flash_errors import flash_errors
from ....cursor import db

class ProcessoEditarNegocio:    
    def exibir(processo_id):        
        form = EditarProcessoForm()

        processo = Processo(processo_id = processo_id)

        if request.method == 'GET':

            if processo.get_id() is not None:
                form.processo_nome.data = processo.nome
                form.processo_id.data = processo.get_id()
            else:
                return redirect(url_for('processo_listar_2'))

        elif form.validate_on_submit():
            processo.nome = form.processo_nome.data
            processo.salva()

            return redirect(url_for('processo_listar_2'))
        else:
            flash_errors(form)

        return render_template('processo_editar_2.html', form=form)