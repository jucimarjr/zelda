from flask import render_template, flash, redirect, url_for
from ...utils.flash_errors import flash_errors
from ...cursor import db

class FuncionalidadeListarNegocio:

    def exibir():
        funcionalidades = db.get_funcionalidades()
        return render_template('funcionalidade_listar.html', funcionalidades=funcionalidades)
