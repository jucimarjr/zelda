from .crud_processo_form import CrudProcesso
from ...tables.processo_equipe_3.processo_modelo import Processo
from ...utils.flash_errors import flash_errors
from ...cursor import db
from ...utils.zelda_modelo import ZeldaModelo
from flask import render_template, flash, redirect, url_for

class CrudProcessoDeletarNegocio:

    def exibir(id):

        processo = Processo()

        processo.processo_id = id

        processo.deletar()

        return redirect(url_for('processo_crud_recuperar'))
