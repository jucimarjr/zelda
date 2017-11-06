from flask import render_template, flash, redirect, url_for, request
from ...tables.funcionalidade.funcionalidade_modelo import Funcionalidade 
from .funcionalidade_editar_form import EditarFuncionalidadeForm
from ..funcionalidade_cadastrar.funcionalidade_cadastrar_form import CadastrarFuncionalidadeForm
from ...utils.flash_errors import flash_errors
from ...utils.criptografador import Criptografador
from ...utils.zelda_modelo import ZeldaModelo
import os

from app import app, ALLOWED_EXTENSIONS

class FuncionalidadeEditarNegocio:
    def exibir(funcionalidade_id):

        form = EditarFuncionalidadeForm()
        funcionalidade = Funcionalidade(funcionalidade_id = funcionalidade_id)
        sistemas = ZeldaModelo.lista_sistemas()
        form.funcionalidade_sistema.choices = [(s.get_id(), s.nome) for s in sistemas]

        if request.method == 'GET':

            if funcionalidade.get_id() is not None:
                form.funcionalidade_nome.data = funcionalidade.nome
                form.funcionalidade_desc.data = funcionalidade.desc
                form.funcionalidade_caminho.data = funcionalidade.caminho
                form.funcionalidade_sistema.data = funcionalidade.get_sistema()
                
            else:
                return redirect(url_for('funcionalidade_listar'))

        print(funcionalidade.get_codigo())

        if form.validate_on_submit():
            funcionalidade.nome = form.funcionalidade_nome.data
            funcionalidade.desc = form.funcionalidade_desc.data
            funcionalidade.caminho = form.funcionalidade_caminho.data
            funcionalidade.set_sistema(form.funcionalidade_sistema.data)
            # funcionalidade.codigo

            funcionalidade.salva()
            return redirect(url_for('funcionalidade_listar'))
        else:
            flash_errors(form)

        return render_template('funcionalidade_editar.html', form=form)
