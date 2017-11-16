from flask import Flask, render_template, flash, redirect, url_for, request
from ....utils.flash_errors import flash_errors
from ....tables.equipe7.documento.documento_modelo import Documento

class DocumentoRemoverNegocio:

    def exibir(documento_id):
        documento = Documento(documento_id)
        if documento.get_id() is None:
            return redirect(url_for('documento_listar'))

        if request.method == 'POST':
            documento.deleta()
            return redirect(url_for('documento_listar'))

        return render_template('equipe7_documento_remover.html', documento = documento)
    
