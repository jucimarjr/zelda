from flask import render_template, flash, redirect, url_for, request
from ...utils.flash_errors import flash_errors
from ...tables.funcionario.funcionario_modelo import Funcionario

class FuncionarioRemoverNegocio:

    def exibir(func_id):
        funcionario = Funcionario(func_id)
        if funcionario.get_id() is None:
            return redirect(url_for('funcionario_listar'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            funcionario.desativa()
        else:
            return render_template('funcionario_desativar.html', funcionario=funcionario)
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra
    página de listagem"""
        return redirect(url_for('funcionario_listar'))