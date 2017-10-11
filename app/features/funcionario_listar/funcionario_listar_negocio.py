from flask import render_template, redirect, url_for
from ...cursor import db

class FuncionarioListarNegocio:
    def exibir():        
        funcionarios = db.get_funcionarios()
        return render_template('funcionario_listar.html', funcionarios=funcionarios)