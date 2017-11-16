from flask import render_template, flash, redirect, url_for
from .usuario_cadastrar_form import CadastrarDocumentoForm
from ...cursor import db
from ...utils.flash_errors import flash_errors
from ...tables.documento.documento_modelo import Documento
from ...utils.zelda_modelo import ZeldaModelo
from ...utils.files import flash_errors_extensao
from flask_json import json_response

class DocumentoCadastrarNegocio:
    
    def exibir():
        
        form = CadastrarDocumentoForm()
        
        if form.validate_on_submit():
            documento = Documento()
            documento.tipo = form.documento_tipo.data
            documento.descricao = form.documento_descricao.data
            documento.salva()
            
            return redirect(url_for('equipe8_documento_cadastrar'))
        else:
            flash_errors(form)
        
        return render_template('equipe_8_documento_criar.html', form=form)
