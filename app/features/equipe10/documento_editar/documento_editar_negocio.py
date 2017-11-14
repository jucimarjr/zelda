from .documento_editar_form import EditarDocumentoForm
from ....tables.equipe10.documento.documento_modelo import Documento
from ....utils.flash_errors import flash_errors
from ....utils.files import flash_errors_extensao

from flask import render_template, flash, redirect, url_for

class DocumentoEditarNegocio:

    def exibir(documento_id):
        form = EditarDocumentoForm()

        documento = Documento(documento_id)
        if documento.get_id() is None:
            return redirect(url_for('documento_listar'))

        if form.validate_on_submit():
            documento.tipo = form.documento_tipo.data
            documento.desc = form.documento_desc.data

            documento.salva()

            if form.file.data is not None:
                documento.set_foto(form.file.data)
                if documento.get_caminho_foto() is None:
                    flash_errors_extensao()
                    return render_template('documento_editar.html', form=form)

            return redirect(url_for('documento_listar'))
        else:
            flash_errors(form)

        form.documento_tipo.data = documento.tipo
        form.documento_desc.data = documento.desc
        return render_template('documento_editar.html', form=form)