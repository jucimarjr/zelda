from flask import render_template, flash, redirect, url_for
from ...utils.flash_errors import flash_errors
from ...utils.zelda_modelo import ZeldaModelo

class FuncionalidadeListarNegocio:

    def exibir():
        funcionalidades = ZeldaModelo.lista_funcionalidades()
        return render_template('funcionalidade_listar.html', funcionalidades = funcionalidades)
