from flask import render_template, flash, redirect, url_for
from ....utils.zelda_modelo import ZeldaModelo

class ProcessoListarNegocio:
    def exibir():
        processos = ZeldaModelo.lista_processos();
        return render_template('processo_listar.html', processos=processos, ZeldaModelo=ZeldaModelo)