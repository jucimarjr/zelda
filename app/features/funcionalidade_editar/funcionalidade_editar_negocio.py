from flask import render_template, flash, redirect, url_for
from .funcionalidade_editar_form import EditarFuncionalidadeForm
from ...utils.flash_errors import flash_errors
from ...utils.criptografador import Criptografador
from ...utils.zelda_modelo import ZeldaModelo
import os

from app import app, ALLOWED_EXTENSIONS

class FuncionalidadeEditarNegocio:
    def exibir():
        form = EditarFuncionalidadeForm()

        sistemas = ZeldaModelo.lista_sistemas()
        form.funcionalidade_sistema.choices = [(s.get_id(), s.nome) for s in sistemas]

        if form.validate_on_submit():

            funcionalidade = Funcionalidade()
            funcionalidade.nome = form.funcionalidade_nome.data
            funcionalidade.desc = form.funcionalidade_desc.data
            funcionalidade.set_sistema(form.funcionalidade_sistema.data)

            funcionalidade.salva()
            return redirect(url_for('funcionalidade_listar'))
        else:
            flash_errors(form)

        return render_template('funcionalidade_editar.html', form=form)
