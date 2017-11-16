from flask import render_template, flash, redirect, url_for
from .documento_cadastrar_form import CadastrarDocumentoForm
from ....cursor import db
from ....utils.flash_errors import flash_errors
from ....tables.equipe9.processo.processo_modelo import Processo
from ....tables.equipe9.documento.documento_modelo import Documento
from ....utils.zelda_modelo import ZeldaModelo


class DocumentoCadastrarNegocio:

    def exibir():

        form = CadastrarDocumentoForm()

        processos = ZeldaModelo.lista_processos()

        form.documento_processo.choices = [(p.get_id(),p.processo_tipo) for p in processos]

        if form.validate_on_submit():

            documento = Documento()

            documento.tipo = form.documento_tipo.data
            documento.descricao = form.documento_descricao.data
            documento.caminho = form .documento_caminho.data
            documento.set_processo( Processo(form.documento_processo.data) )
            documento.salva()

            return redirect(url_for('documento_listar'))

        else:
            flash_errors(form)

        return render_template('equipe9_documento_criar.html', form=form)
