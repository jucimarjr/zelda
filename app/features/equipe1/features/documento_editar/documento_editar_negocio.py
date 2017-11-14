from ...tables.documento.documento_modelo import Documento
from ...tables.processo.processo_modelo import Processo
from flask import render_template, redirect, url_for
from .....utils.flash_errors import flash_errors
from .documento_editar_form import DocumentoEditarForm

class DocumentoEditarNegocio:
    def exibir(processo_id, documento_id):
        form = DocumentoEditarForm()

        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('equipe1_processo_listar'))

        documento = Documento(id_documento = documento_id)
        if documento.get_id() is None:
            return redirect(url_for('equipe1_processo_editar', processo_id = processo_id))            

        form.documento_tipo.choices = [ (index, Documento.lista_tipos[index]) for index in range(0, len(Documento.lista_tipos))]

        if form.validate_on_submit():
            documento.tipo = form.documento_tipo.data
            documento.descricao = form.documento_desc.data
            documento.caminho = form.documento_caminho.data
            documento.salva()

            return redirect(url_for('equipe1_processo_editar', processo_id = processo_id))
        else:
            flash_errors(form)

        form.documento_tipo.data = documento.tipo
        form.documento_desc.data = documento.descricao
        form.documento_caminho.data = documento.caminho
        return render_template('equipe1_documento_editar.html', processo = processo, form = form)