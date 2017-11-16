from .processo_cadastrar_form import CadastrarProcessoForm
from .....tables.equipe_11.processo.processo_modelo import Processo
from .....utils.flash_errors import flash_errors
from .....utils.zelda_modelo_11 import ZeldaModelo
from .....utils.files import flash_errors_extensao

from flask import render_template, flash, redirect, url_for

class processoCadastrarNegocio:

    def exibir():
        form = CadastrarProcessoForm()

        sistemas = ZeldaModelo.lista_sistemas()

        if form.validate_on_submit():

            processo = Processo()
            processo.processo_tipo = form.processo_tipo.data
            processo.processo_desc = form.processo_desc.data
            #processo.usuario_id = 
            processo.salva()
            return redirect(url_for('processo_listar'))
        else:
            flash_errors(form)

        return render_template('processo_criar_11.html', form=form)
