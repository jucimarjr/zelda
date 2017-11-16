from app.tables.equipe4.tables.documento.documento_modelo import Documento
from app.tables.equipe4.tables.processo.processo_modelo import Processo
from flask import render_template, redirect, url_for
from .....utils.flash_errors import flash_errors
from .documento_editar_form import DocumentoEditarForm

class DocumentoEditarNegocio:
    def exibir(processo_id, documento_id):
        form = DocumentoEditarForm()

        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar_4'))

        documento = Documento(documento_id = documento_id)
        if documento.get_id() is None:
            return redirect(url_for('processo_editar_4', processo_id = processo_id))

        form.documento_tipo.choices = [ (index, Documento.lista_tipos[index]) for index in range(0, len(Documento.lista_tipos))]

        if form.validate_on_submit():
            documento.tipo = form.documento_tipo.data
            documento.descricao = form.documento_descricao.data
            documento.caminho = form.documento_link.data
            documento.salva()

            return redirect(url_for('processo_editar_4', processo_id = processo_id))
        else:
            flash_errors(form)

        form.documento_tipo.data = documento.tipo
        form.documento_desc.data = documento.descricao
        form.documento_caminho.data = documento.caminho
        return render_template('equipe4_documento_editar.html', processo = processo, form = form)
