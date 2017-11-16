from flask import render_template, flash, redirect, url_for, request
from .documento_editar_form import EditarDocumentoForm
from ....tables.equipe_2.documento.documento_modelo import DocumentoDois
from ....utils.flash_errors import flash_errors
from ....cursor import db

class DocumentoEditarNegocio:
    def exibir(documento_id):
        form = EditarDocumentoForm()

        documento = DocumentoDois(documento_id = documento_id)

        if request.method == 'GET':

            if documento.get_id() is not None:
                form.documento_nome.data = documento.nome
                form.documento_id.data = documento.get_id()
            else:
                return redirect(url_for('documento_listar_2'))

        elif form.validate_on_submit():
            documento.nome = form.documento_nome.data
            documento.salva()

            return redirect(url_for('documento_listar_2'))
        else:
            flash_errors(form)

        return render_template('documento_editar_2.html', form=form)
