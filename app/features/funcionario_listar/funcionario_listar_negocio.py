from flask import render_template, redirect, url_for
from ...utils.zelda_modelo import ZeldaModelo

class FuncionarioListarNegocio:
    def exibir():
        funcionarios = ZeldaModelo.lista_funcionarios()
        return render_template('funcionario_listar.html', funcionarios=funcionarios)