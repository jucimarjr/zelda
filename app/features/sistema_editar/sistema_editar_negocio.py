from .sistema_editar_form import EditarSistemaForm
from ...tables.sistema.sistema_modelo import Sistema
from ...utils.flash_errors import flash_errors

from flask import render_template, flash, redirect, url_for

class SistemaEditarNegocio:

    def exibir(sistema_id):
        form = EditarSistemaForm()

        sistema = Sistema(sistema_id)
        if sistema.get_id() is None:
            return redirect(url_for('sistema_listar'))

        if form.validate_on_submit():
            sistema.nome = form.sistema_nome.data
            sistema.desc = form.sistema_desc.data
            sistema.prefixo = form.sistema_prefixo.data

            sistema.salva()
            return redirect(url_for('sistema_listar'))
        else:
            flash_errors(form)

        form.sistema_nome.data = sistema.nome
        form.sistema_desc.data = sistema.desc
        form.sistema_prefixo.data = sistema.prefixo
        return render_template('sistema_editar.html', form=form)
