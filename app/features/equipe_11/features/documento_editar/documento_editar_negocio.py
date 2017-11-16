from flask import render_template, flash, redirect, url_for, request
from .....tables.equipe_11.documento.documento_modelo import Documento
from .documento_editar_form import EditarDocumentoForm
from ..documento_cadastrar.documento_cadastrar_form import CadastrarDocumentoForm
from .....utils.flash_errors import flash_errors
from .....utils.criptografador import Criptografador
from .....utils.zelda_modelo_11 import ZeldaModelo
from .....utils.files import flash_errors_extensao

class DocumentoEditarNegocio:
    def exibir(documento_id):

        form = EditarDocumentoForm()
        documento = Documento(documento_id = documento_id)

        if request.method == 'GET':

            if documento.get_id() is not None:
                form.documento_tipo.data = documento.documento_tipo
                form.documento_desc.data = documento.documento_desc

            else:
                return redirect(url_for('documento_listar'))


        if form.validate_on_submit():
            documento.documento_tipo = form.documento_tipo.data
            documento.documento_desc = form.documento_desc.data
            documento.salva()

            return redirect(url_for('documento_listar'))
        else:
            flash_errors(form)

        return render_template('documento_editar_11.html', form=form)
