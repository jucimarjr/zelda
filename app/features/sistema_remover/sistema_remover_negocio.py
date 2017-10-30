from flask import render_template, flash, redirect, url_for, request
from ...utils.flash_errors import flash_errors
from ...tables.sistema.sistema_modelo import Sistema

class SistemaRemoverNegocio:

    def exibir(sistema_id):
        sistema = Sistema(sistema_id)

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            sistema.sitema_id = 1
        else:
            return render_template('sistema_desativar.html', sistema=sistema)
        
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra página de listagem"""
        return redirect(url_for('sistema_listar'))
