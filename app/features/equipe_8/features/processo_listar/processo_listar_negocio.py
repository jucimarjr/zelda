from flask import render_template, flash, redirect, url_for
from .....utils.flash_errors import flash_errors
from .....utils.zelda_modelo import ZeldaModelo

class ProcessoListarNegocio:
    
    def exibir():
        processos = ZeldaModelo.lista_processos()
        return render_template('equipe_8_processo_listar.html', processos = processos)
