from flask import render_template, flash, redirect, url_for
from ...utils.flash_errors import flash_errors
from ...utils.zelda_modelo import ZeldaModelo

class SistemaListarNegocio:
    def exibir():
        sistemas = ZeldaModelo.lista_sistemas();
        return render_template('sistema_listar.html', sistemas=sistemas, ZeldaModelo=ZeldaModelo)