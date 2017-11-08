from .funcionalidade_cadastrar_form import CadastrarFuncionalidadeForm
from ...tables.funcionalidade.funcionalidade_modelo import Funcionalidade
from ...utils.flash_errors import flash_errors
from ...utils.zelda_modelo import ZeldaModelo
from ...utils.files import flash_errors_extensao

from flask import render_template, flash, redirect, url_for

class FuncionalidadeCadastrarNegocio:

    def exibir():
        form = CadastrarFuncionalidadeForm()

        sistemas = ZeldaModelo.lista_sistemas()
        form.funcionalidade_sistema.choices = [(s.get_id(), s.nome) for s in sistemas]

        if form.validate_on_submit():

            funcionalidade = Funcionalidade()
            funcionalidade.salva()
            funcionalidade.nome = form.funcionalidade_nome.data
            funcionalidade.desc = form.funcionalidade_desc.data 
            funcionalidade.set_sistema(form.funcionalidade_sistema.data)
            funcionalidade.salva()

            if form.funcionalidade_imagem.data is not None:
                funcionalidade.set_imagem(form.funcionalidade_imagem.data)
                if funcionalidade.get_caminho_imagem() is None:
                    flash_errors_extensao()
                    return render_template('funcionalidade_criar.html', form=form)

            return redirect(url_for('funcionalidade_listar'))
        else:
            flash_errors(form)

        return render_template('funcionalidade_criar.html', form=form)
