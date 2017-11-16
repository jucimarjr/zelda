from flask import render_template, flash, redirect, url_for
from .usuario_editar_form import EditarUsuarioForm
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...tables.perfil.perfil_modelo import Perfil
from ...utils.criptografador import Criptografador
from ...utils.zelda_modelo import ZeldaModelo
from ...utils.files import flash_errors_extensao

from app import app

class UsuarioEditarNegocio:
    def exibir(user_id):
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
                
        return render_template('equipe_8_documento_editar.html', form=form)
