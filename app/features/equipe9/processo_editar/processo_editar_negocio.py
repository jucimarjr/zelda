from flask import render_template, flash, redirect, url_for
from .processo_editar_form import EditarProcessoForm
from ....utils.flash_errors import flash_errors
from ....tables.equipe9.processo.processo_modelo import Processo
from ....tables.usuario.usuario_modelo import Usuario
from ....utils.zelda_modelo import ZeldaModelo

from app import app

class ProcessoEditarNegocio:
    def exibir(processo_id):
        form = EditarProcessoForm()

        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar'))

        usuarios = ZeldaModelo.lista_usuarios()

        form.processo_usuario.choices = [(p.get_id(),p.login) for p in usuarios]

        if form.validate_on_submit():
            processo.tipo = form.processo_tipo.data
            processo.descricao = form.processo_descricao.data
            processo.set_usuario( Usuario(form.processo_usuario.data) )
            processo.salva()

            return redirect(url_for('processo_listar'))

        else:
            flash_errors(form)

        form.processo_usuario.default = int(processo.get_usuario().get_id())
        form.process()

        form.processo_tipo.data = processo.processo_tipo

        return render_template('equipe9_processo_editar.html', form=form)
