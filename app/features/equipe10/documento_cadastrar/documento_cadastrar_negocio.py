from .documento_cadastrar_form import CadastrarDocumentoForm
from ....tables.equipe10.documento.documento_modelo import Documento
from ....utils.files import flash_errors_extensao
from ....utils.flash_errors import flash_errors

from flask import render_template, flash, redirect, url_for

class DocumentoCadastrarNegocio:

    def exibir():
        form = CadastrarDocumentoForm()

        if form.validate_on_submit():

            documento = Documento()
            documento.tipo = form.processo_tipo.data
            documento.desc = form.processo_desc.data


            documento.salva()

            if form.file.data is not None:
                documento.set_foto(form.file.data)
                if documento.get_caminho_foto() is None:
                    flash_errors_extensao()
                    return render_template('documento_criar.html', form=form)

            return redirect(url_for('documento_listar'))
        else:
            flash_errors(form)

        return render_template('documento_criar.html', form=form)