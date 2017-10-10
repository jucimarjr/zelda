from flask import render_template, flash, redirect, url_for
from ...utils.flash_errors import flash_errors
from ...authentication import verifica_sessao
from ...cursor import db

class FuncionarioRemoverNegocio:

    def exibir(func_id):
        if verifica_sessao() == True:
            return redirect(url_for('login'))

        funcionario = db.get_funcionario(func_id)
        if funcionario is None:
            return redirect(url_for('funcionario_listar'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            db.deleta_funcionario(func_id)
        else:
            return render_template('funcionario_desativar.html', funcionario=funcionario)
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra
    página de listagem"""
        return redirect(url_for('funcionario_listar'))