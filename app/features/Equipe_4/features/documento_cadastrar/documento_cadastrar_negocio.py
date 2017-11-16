from app.tables.equipe4.tables.documento.documento_modelo import Documento
from app.tables.equipe4.tables.processo.processo_modelo import Processo
from flask import render_template, redirect, url_for
from .....utils.flash_errors import flash_errors
from .documento_cadastrar_form import DocumentoCadastrarForm

class DocumentoCadastrarNegocio:
    def exibir(processo_id):
        form = DocumentoCadastrarForm()

        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('processo_listar_4'))

        form.documento_tipo.choices = [ (index, Documento.lista_tipos[index]) for index in range(0, len(Documento.lista_tipos))]
        form.documento_tipo.data = 0

        if form.validate_on_submit():
            documento = Documento(processo_id = processo.get_id())
            documento.tipo = form.documento_tipo.data
            documento.descricao = form.documento_descricao.data
            documento.link = form.documento_link.data
            documento.salva()

            processo.adiciona_documento(documento)
            return redirect(url_for('processo_editar_4', processo_id = processo_id))
        else:
            flash_errors(form)

        return render_template('equipe4_documento_criar.html', processo = processo, form = form)
