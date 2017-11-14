from .crud_processo_form import CrudProcesso
from ...tables.processo_equipe_3.processo_modelo import Processo
from ...utils.flash_errors import flash_errors
from ...cursor import db
from ...utils.zelda_modelo import ZeldaModelo
from flask import render_template, flash, redirect, url_for

class CrudProcessoEditarNegocio:

    def exibir(id):
        
        form = CrudProcesso()

        processo = Processo()

        if form.processo_tipo.data != "" and form.processo_descricao.data != "" and form.processo_nome_aluno.data != "" and form.processo_tipo.data != None and form.processo_descricao.data != None and form.processo_nome_aluno.data != None:
            processo.processo_nome_aluno = form.processo_nome_aluno.data
            processo.processo_tipo = form.processo_tipo.data
            processo.processo_descricao = form.processo_descricao.data
            processo.processo_id = id
            processo.edit()
        else:
            print(form.processo_tipo.data)
            flash_errors(form)

        return render_template('equipe_3_editar_processo.html', form=form)
