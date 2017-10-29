from flask import Flask,render_template, flash, redirect, url_for, request
from ...utils.flash_errors import flash_errors
from ...cursor import db

class PerfilRemoverNegocio:

    def exibir(perfil_id):
        perfil = db.get_perfil_pelo_id(perfil_id)
        if perfil is None:
            return redirect(url_for('perfil_listar'))

        if request.method == 'POST':
            db.deleta_perfil(perfil_id)
        else:
            return render_template('perfil_remover.html',perfil=perfil)

        return redirect(url_for('perfil_listar'))
