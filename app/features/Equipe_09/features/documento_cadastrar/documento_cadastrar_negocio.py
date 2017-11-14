from flask import render_template, flash, redirect, url_for
from .documento_cadastrar_form import CadastrarDocumentoForm
from ...utils.flash_errors import flash_errors
from ...tables.documento.documento_modelo import Documento

class DocumentoCadastrarNegocio:
    def exibir():
        form = CadastrarDocumentoForm()

        if form.validate_on_submit():
            documento = Documento()
            documento.tipo = form.documento_tipo.data
            documento.descricao = form.documento_descricao.data
            documento.salva()

            return redirect(url_for('documento_listar'))
        else:
            flash_errors(form)

        return render_template('documento_criar.html', form=form)
