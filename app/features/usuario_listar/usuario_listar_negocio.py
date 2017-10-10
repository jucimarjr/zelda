from flask import render_template, flash, redirect, url_for
from ...utils.flash_errors import flash_errors
from ...authentication import verifica_sessao
from ...cursor import db

class UsuarioListarNegocio:

    def exibir():
        if(verifica_sessao() == True):
            return redirect(url_for('login'))

        usuarios = db.get_usuarios()
        return render_template('usuario_listar.html', usuarios=usuarios)