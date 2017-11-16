from flask import render_template, flash, redirect, url_for
from .documento_editar_form import EditarDocumentoForm
from ....utils.flash_errors import flash_errors
from ....tables.equipe7.documento.documento_modelo import Documento
from ....tables.equipe7.processo.processo_modelo import Processo
from ....utils.zelda_modelo import ZeldaModelo

from app import app

class DocumentoEditarNegocio:
    
    def exibir(documento_id):
        form = EditarDocumentoForm()

        documento = Documento(documento_id)

        if documento.get_id() is None:
            return redirect(url_for('documento_listar'))

        processos = ZeldaModelo.lista_processos()

        form.documento_processo.choices = [(p.get_id(),p.processo_tipo) for p in processos]
      
        if form.validate_on_submit():
            documento.set_processo(Processo(form.documento_processo.data))
            documento.tipo = form.documento_tipo.data
            documento.descricao = form.documento_desc.data
            documento.caminho = form.documento_caminho.data
            documento.salva()

            return redirect(url_for('documento_listar'))

        else:
            flash_errors(form)
        
        form.documento_processo.default = int(documento.get_processo().get_id())
        form.process()

        form.documento_tipo.data = documento.documento_tipo
                
        return render_template('equipe7_documento_editar.html', form=form)
