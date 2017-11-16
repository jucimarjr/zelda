from .documento_cadastrar_form import CadastrarDocumentoForm
from .....tables.equipe_11.documento.documento_modelo import Documento
from .....utils.flash_errors import flash_errors
from .....utils.zelda_modelo_11 import ZeldaModelo
from .....utils.files import flash_errors_extensao

from flask import render_template, flash, redirect, url_for

class DocumentoCadastrarNegocio:

    def exibir():
        form = CadastrarDocumentoForm()

        sistemas = ZeldaModelo.lista_sistemas()

        if form.validate_on_submit():

            documento = Documento()
            documento.documento_tipo = form.documento_tipo.data
            documento.documento_desc = form.documento_desc.data
            #documento.usuario_id =
            documento.salva()
            return redirect(url_for('documento_listar'))
        else:
            flash_errors(form)

        return render_template('documento_criar_11.html', form=form)
