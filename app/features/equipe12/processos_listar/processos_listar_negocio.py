from flask import render_template, redirect, url_for
from ....utils.processos_modelo_12 import ProcessaModelo

class ProcessoListarNegocio:
    def exibir():
        processos = ProcessaModelo.listar_processos_12()
        return render_template('processos_listar_12.html',processos=processos)
