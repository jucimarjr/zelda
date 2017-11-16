from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import ProcessoCadastrarForm
from ....utils.flash_errors import flash_errors
from ....tables.equipe_2.processo.processo_modelo import ProcessoDois
from ....authentication import *

class ProcessoCadastrarNegocio:
    def exibir():
        form = ProcessoCadastrarForm()

        if form.validate_on_submit():
            processo = ProcessoDois()
            processo.__descricao = form.processo_descricao.data
            processo.__tipo = form.processo_tipo.data
            user = retorna_usuario()
            processo.__usuario_id = user.get_id()
            processo.salva_dois(form.processo_descricao.data, form.processo_tipo.data, None, user.get_id())

            return redirect(url_for('processo_listar_2'))
        else:
            flash_errors(form)

        return render_template('processo_cadastrar_2.html', form=form)