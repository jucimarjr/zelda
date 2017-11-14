from flask import render_template, flash, redirect, url_for, request
from ....utils.flash_errors import flash_errors
from ....tables.equipe10.documento.documento_modelo import Documento

class DocumentoRemoverNegocio:
    def exibir(documento_id):
        documento = Documento(documento_id)

        if documento.get_id() is None:
            return redirect(url_for('documento_listar'))

        if request.method == 'POST':
            documento.deleta()
        else:
            return render_template('documento_remover.html',documento=documento)

        return redirect(url_for('documento_listar'))