from flask import render_template, flash, redirect, url_for, request
from .documento_editar_form import EditarDocumentoForm
from ....tables.equipe_2.documento.documento_modelo import DocumentoDois
from ....utils.flash_errors import flash_errors
from ....cursor import db
from ....authentication import *

class DocumentoEditarNegocio:
    def exibir(documento_id):
        form = EditarDocumentoForm()

        documento = DocumentoDois(documento_id = documento_id)

        if request.method == 'GET':

            if documento.get_id() is not None:
                form.documento_descricao.data = documento.get_descricao()
                form.documento_tipo.data = documento.get_tipo()
                form.documento_id.data = documento.get_id()
            else:
                return redirect(url_for('documento_listar_2'))

        elif form.validate_on_submit():
            documento.__descricao = form.documento_descricao.data
            documento.__tipo = form.documento_tipo.data
            documento.__id = documento_id
            documento.salva_dois(form.documento_descricao.data, form.documento_tipo.data, documento_id) 

            return redirect(url_for('documento_listar_2'))
        else:
            flash_errors(form)

        return render_template('documento_editar_2.html', form=form)
