from flask import render_template, flash, redirect, url_for
from .....utils.flash_errors import flash_errors
from .....utils.zelda_modelo_11 import ZeldaModelo

class ProcessoListarNegocio:

    def exibir():
        processos = ZeldaModelo.lista_processos()
        return render_template('processo_listar_11.html', processos = processos)
