from flask import render_template, redirect, url_for
from ....utils.zelda_modelo_13 import ProcessoModelo

class ProcessoListarNegocio:
    def exibir():
        processos = ProcessoModelo.listar_processos()
        return render_template('processos_listar_12.html',processos=processos)

