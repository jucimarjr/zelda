from flask import render_template, flash, redirect, url_for
from .perfil_criar_form import CadastrarPerfilForm
from ...utils.flash_errors import flash_errors
from ...tables.perfil.perfil_modelo import Perfil
from ...tables.permissao.permissao_modelo import Permissao
from ...utils.criptografador import Criptografador
from ...utils.zelda_modelo import ZeldaModelo

class PerfilCadastrarNegocio:

    def exibir():
        form = CadastrarPerfilForm()

        funcionalidades = ZeldaModelo.lista_funcionalidades()
        form.funcionalidades_ids.choices = [(f.get_id(), f.nome) for f in funcionalidades]

        if form.validate_on_submit():
            perfil = Perfil()
            perfil.nome = form.perfil_nome.data
            perfil.salva()
            perfil.altera_funcionalidades(form.funcionalidades_ids.data)

            return redirect(url_for('perfil_listar'))

        else:
            flash_errors(form)

        return render_template('perfil_criar.html', form=form)
