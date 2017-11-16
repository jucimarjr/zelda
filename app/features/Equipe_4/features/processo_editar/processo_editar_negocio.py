from flask import render_template, flash, redirect, url_for
from .processo_editar_form import EditarProcessoForm
from app.utils.flash_errors import flash_errors
from app.tables.equipe4.tables.processo.processo_modelo import Processo
from app.utils.zelda_modelo_4 import ZeldaModelo



from app import app

class ProcessoEditarNegocio:
    def exibir(processo_id):
        form = EditarProcessoForm()

        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar_4'))

        if form.validate_on_submit():
            processo.tipo = form.processo_tipo.data
            processo.desc = form.processo_desc.data
            processo.salva()

            return redirect(url_for('processo_listar_4'))

        else:
            flash_errors(form)

        return render_template('equipe4_processo_editar.html', form=form)
