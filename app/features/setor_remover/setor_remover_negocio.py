from flask import render_template, flash, redirect, url_for, request
from .setor_remover_form import RemoverSetorForm
from ...utils.flash_errors import flash_errors
from ...authentication import verifica_sessao
from ...cursor import db

class SetorRemoverNegocio:

    def exibir(setor_id):
        if verifica_sessao() == True:
            return redirect(url_for('login'))

        setor = db.get_setor(setor_id)
        if setor is None:
            return redirect(url_for('setor_listar'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            db.deleta_setor(setor_id)
        else:
            return render_template('setor_desativar.html', setor=setor)
        
        """Se o método foi GET ou o form deu erro de submissão, redireciona pra página de listagem"""
        return redirect(url_for('setor_listar'))
