from flask import render_template, flash, redirect, url_for
from app.utils.flash_errors import flash_errors
from app.utils.zelda_modelo_4 import ZeldaModelo

class ProcessoListarNegocio:

    def exibir():
        processos = ZeldaModelo.lista_processos()
        return render_template('equipe4_processo_listar.html', processos = processos)
