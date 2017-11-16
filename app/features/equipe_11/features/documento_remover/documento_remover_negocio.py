from flask import render_template, flash, redirect, url_for, request
from .documento_remover_form import RemoverDocumentoForm
from .....utils.flash_errors import flash_errors
from .....tables.equipe_11.documento.documento_modelo import Documento

class DocumentoRemoverNegocio:

    def exibir(documento_id):
        documento_aux = eval(documento_id)
        documento = documento(documento_aux)
        if documento.get_id() is None:
            return redirect(url_for('documento_listar'))

        if request.method == 'POST':
            documento.desativa()
        else:
            return render_template('documento_desativar_11.html', documento = documento)

        return redirect(url_for('documento_listar'))
