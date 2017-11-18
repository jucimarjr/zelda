from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import CadastrarProcessoForm
from ....utils.flash_errors import flash_errors
from ....tables.equipe5.processo_modelo import Processo
from ....authentication import *

class ProcessoCadastrarNegocio:
    def exibir():
        form = CadastrarProcessoForm()

        if form.validate_on_submit():
            processo = Processo()
            processo.__descricao = form.processo_descricao.data
            processo.__tipo = form.processo_tipo.data
            user = retorna_usuario()
            processo.__usuario_id = user.get_id()
            processo.salva(form.processo_descricao.data, form.processo_tipo.data, None, user.get_id())

            return redirect(url_for('processo_listar_5'))
        else:
            flash_errors(form)

        return render_template('processo_criar_5.html', form=form)
