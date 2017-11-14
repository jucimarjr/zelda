from .processos_cadastrar_form import CadastrarProcessoForm
from ....tables.processos.processos_modelo import Processo
from ....utils.flash_errors import flash_errors
from ....utils.processos_modelo_12 import ProcessaModelo
from ....utils.files import flash_errors_extensao

from flask import render_template, flash, redirect, url_for

class ProcessoCadastrarNegocio:

    def exibir():
        form  = CadastrarProcessoForm()

        if form.validate_on_submit():
            processo = Processo()

            processo.tipo = form.processo_tipo.data
            processo.desc = form.processo_desc.data


            processo.salva()
            return redirect(url_for('processos_listar_12'))
        else:
            flash_errors(form)

        return render_template('processos_criar_12.html', form=form)
