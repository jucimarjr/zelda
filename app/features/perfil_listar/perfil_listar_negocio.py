from flask import render_template, flash, redirect, url_for
from ...cursor import db
from ...utils.zelda_modelo import ZeldaModelo

class PerfilListarNegocio:
    def exibir():
        perfis = db.get_perfil()
        return render_template('perfil_listar.html', perfis = perfis)
