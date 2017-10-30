from flask import render_template, flash, redirect, url_for
from ...utils.flash_errors import flash_errors
from ...utils.zelda_modelo import ZeldaModelo

class UsuarioListarNegocio:

    def exibir():
        usuarios = ZeldaModelo.lista_usuarios()
        return render_template('usuario_listar.html', usuarios = usuarios)