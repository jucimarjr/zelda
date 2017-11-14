from .processos_cadastrar_form import CadastrarProcessoForm
from ....tables.processos.processos_modelo import Processo
from ....utils.flash_errors import flash_errors
from ....utils.zelda_modelo import ZeldaModelo
from ....utils.files import flash_errors_extensao

from flask import render_template, flash, redirect, url_for

class ProcessoCadastrarNegocio:

    def exibir():
        form  = CadastrarProcessoForm()
        return render_template('processos_criar_12.html', form=form)
