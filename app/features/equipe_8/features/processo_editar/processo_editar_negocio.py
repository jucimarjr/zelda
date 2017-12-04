from flask import render_template, flash, redirect, url_for
from .processo_editar_form import EditarProcessoForm
from .....utils.flash_errors import flash_errors
from ...tables.processo.processo_modelo import Processo
from .....utils.criptografador import Criptografador
from .....utils.zelda_modelo import ZeldaModelo

from app import app

class ProcessoEditarNegocio:
    def exibir(processo_id):
        form = EditarProcessoForm()
        
        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar'))
        
        if form.validate_on_submit():
            processo.tipo = form.processo_tipo.data
            processo.descricao = form.processo_descricao.data
            processo.salva()

            return redirect(url_for('processo_listar'))
        
        else:
            flash_errors(form)

        return render_template('equipe_8_processo_editar.html', form=form)
