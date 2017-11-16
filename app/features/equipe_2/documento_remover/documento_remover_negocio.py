from flask import render_template, flash, redirect, url_for, request
from .documento_remover_form import RemoverDocumentoForm
from ....utils.flash_errors import flash_errors
from ....cursor import db
from ....tables.equipe_2.documento.documento_modelo import DocumentoDois

class DocumentoRemoverNegocio:

    def exibir(documento_id):
        documento = DocumentoDois(documento_id)
        if documento.get_id() is None:
            return redirect(url_for('documento_listar_2'))

        # Se a página foi acessada por post pelo form do WTForms da própria página
        if request.method == 'POST':
            documento.desativa()
        else:
            return render_template('documento_remover_2.html', documento=documento)

        """Se o método foi GET ou o form deu erro de submissão, redireciona pra página de listagem"""
        return redirect(url_for('documento_listar_2'))
