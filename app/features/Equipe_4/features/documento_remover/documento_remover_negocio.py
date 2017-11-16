from app.tables.equipe4.tables.documento.documento_modelo import Documento
from app.tables.equipe4.tables.processo.processo_modelo import Processo
from flask import render_template, redirect, url_for, request

class DocumentoRemoverNegocio:
    def exibir(processo_id, documento_id):
        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar_4'))

        documento = Documento(id_documento = documento_id)
        if documento.get_id() is None:
            return redirect(url_for('processo_editar_4', processo_id = processo_id))

        if request.method == 'POST':
            processo.remove_documento(documento.get_id())
            return redirect(url_for('processo_editar_4', processo_id = processo_id))

        return render_template('equipe4_documento_remover.html', processo = processo, documento = documento)
