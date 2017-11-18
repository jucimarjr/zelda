from flask import render_template, flash, redirect, url_for
from ...cursor import db
from ...utils.zelda_modelo_5 import ZeldaModelo

class ProcessoListarNegocio:
    def exibir():
        processos = ZeldaModelo.lista_processo_5()

        return render_template('processo_listar_5.html', processos = processos)
