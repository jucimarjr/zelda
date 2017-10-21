from flask import render_template, flash, redirect, url_for, request
from .setor_remover_form import RemoverSetorForm
from ...utils.flash_errors import flash_errors
from ...cursor import db
from ...tables.setor.setor_modelo import Setor

class SetorRemoverNegocio:

    def exibir(setor_id):
        setor = Setor(setor_id)
        if setor.get_id() is None:
            return redirect(url_for('setor_listar'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            setor.desativa()
        else:
            return render_template('setor_desativar.html', setor=setor)
        
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra página de listagem"""
        return redirect(url_for('setor_listar'))
