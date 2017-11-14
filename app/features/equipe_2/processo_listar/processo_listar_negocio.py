from flask import render_template, flash, redirect, url_for
from ....cursor import db
from ....utils.zelda_modelo_2 import ZeldaModeloDois

class ProcessoListarNegocio:
    def exibir():
        processos = ZeldaModeloDois.lista_processo_2(1)
        return render_template('processo_listar_2.html', processos = processos)