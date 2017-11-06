from flask import render_template, flash, redirect, url_for, request
from ...utils.flash_errors import flash_errors
from ...tables.sistema.sistema_modelo import Sistema

class SistemaRemoverNegocio:

    def exibir(sistema_id):
        sistema = Sistema(sistema_id)

        if request.method == 'POST':
            sistema.desativa()
        else:
            return render_template('sistema_desativar.html', sistema=sistema)
        
        return redirect(url_for('sistema_listar'))
