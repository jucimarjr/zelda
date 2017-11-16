from flask import render_template, flash, redirect, url_for
from .documento_cadastrar_form import DocumentoCadastrarForm
from ....utils.flash_errors import flash_errors
from ....tables.equipe_2.documento.documento_modelo import DocumentoDois
from ....utils.zelda_modelo_2 import ZeldaModeloDois
from ....tables.equipe_2.processo.processo_modelo import ProcessoDois
from ....authentication import *

class DocumentoCadastrarNegocio:
    def exibir():
        form = DocumentoCadastrarForm()

        processos = ZeldaModeloDois.lista_processo_2()
        form.documento_processo.choices = [(p.get_id(), p.get_descricao()) for p in processos]
        if form.validate_on_submit():
            documento = DocumentoDois()
            documento.__descricao = form.documento_descricao.data
            documento.__tipo = form.documento_tipo.data
            processo = ProcessoDois(form.documento_processo.data)
            documento.__processo_id = processo.get_id()
            p_id = processo.get_id()
            documento.salva_dois(form.documento_descricao.data, form.documento_tipo.data, p_id)

            return redirect(url_for('documento_listar_2'))
        else:
            flash_errors(form)

        return render_template('documento_cadastrar_2.html', form=form)