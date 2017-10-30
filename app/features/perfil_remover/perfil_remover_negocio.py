from flask import Flask,render_template, flash, redirect, url_for, request
from ...utils.flash_errors import flash_errors
from ...tables.perfil.perfil_modelo import Perfil

class PerfilRemoverNegocio:

    def exibir(perfil_id):
        perfil = Perfil(perfil_id)
        if perfil.get_id() is None:
            return redirect(url_for('perfil_listar'))

        if request.method == 'POST':
            perfil.deleta()
        else:
            return render_template('perfil_remover.html',perfil=perfil)

        return redirect(url_for('perfil_listar'))
