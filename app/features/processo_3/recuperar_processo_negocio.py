from .crud_processo_form import CrudProcesso
from ...tables.processo_equipe_3.processo_modelo import Processo
from ...utils.flash_errors import flash_errors
from ...cursor import db
from ...utils.zelda_modelo import ZeldaModelo
from flask import render_template, flash, redirect, url_for

class CrudProcessoRecuperaNegocio:

    def exibir():
        processo = Processo()

        processos = processo.get_processos()

        return render_template('equipe_3_recuperar_processo.html', processos=processos)
