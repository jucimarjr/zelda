from flask import render_template, flash, redirect, url_for
from .setor_cadastrar_form import CadastrarSetorForm
from ...utils.flash_errors import flash_errors
from ...tables.setor.setor_modelo import Setor

class SetorCadastrarNegocio:
    def exibir():
        form = CadastrarSetorForm()

        if form.validate_on_submit():
            setor = Setor()
            setor.nome = form.setor_nome.data
            setor.salva()

            return redirect(url_for('setor_listar'))
        else:
            flash_errors(form)

        return render_template('setor_criar.html', form=form)