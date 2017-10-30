from flask import render_template, flash, redirect, url_for
from ...utils.zelda_modelo import ZeldaModelo

class PerfilListarNegocio:
    def exibir():
        perfis = ZeldaModelo.lista_perfis()
        return render_template('perfil_listar.html', perfis = perfis)
