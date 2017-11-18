from flask import render_template, flash, redirect, url_for, request
from .processo_editar_form import EditarProcessoForm
from ....tables.equipe5.processo_modelo import Processo
from ....utils.flash_errors import flash_errors
from ....cursor import db
from ....authentication import *

class ProcessoEditarNegocio:
    def exibir(processo_id):
        form = EditarProcessoForm()

        processo = Processo(processo_id = processo_id)

        if request.method == 'GET':

            if processo.get_id() is not None:
                form.processo_descricao.data = processo.get_descricao()
                form.processo_id.data = processo.get_id()
                form.processo_tipo.data = processo.get_tipo()
            else:
                return redirect(url_for('processo_listar_5'))

        elif form.validate_on_submit():
            processo.__descricao = form.processo_descricao.data
            processo.__tipo = form.processo_tipo.data
            processo.__id = processo_id
            user = retorna_usuario()
            processo.__usuario_id = user.get_id()
            processo.salva(form.processo_descricao.data, form.processo_tipo.data, processo_id, user.get_id())
            return redirect(url_for('processo_listar_5'))
        else:
            flash_errors(form)

        return render_template('processo_editar_5.html', form=form)
