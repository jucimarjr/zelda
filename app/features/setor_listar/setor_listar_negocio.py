from flask import render_template, flash, redirect, url_for
from ...cursor import db
from ...utils.zelda_modelo import ZeldaModelo

class SetorListarNegocio:
    def exibir():
        setores = ZeldaModelo.lista_setores()

        return render_template('setor_listar.html', setores = setores)