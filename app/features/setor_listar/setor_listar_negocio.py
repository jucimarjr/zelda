from flask import render_template, flash, redirect, url_for
from ...cursor import db

class SetorListarNegocio:
    def exibir():
        setores = db.get_setores()
        return render_template('setor_listar.html', setores=setores)