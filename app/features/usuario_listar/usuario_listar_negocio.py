from flask import render_template, flash, redirect, url_for
from ...utils.flash_errors import flash_errors
from ...cursor import db

class UsuarioListarNegocio:

    def exibir():
        usuarios = db.get_usuarios()
        return render_template('usuario_listar.html', usuarios=usuarios)