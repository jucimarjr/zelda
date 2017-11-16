from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import CadastrarProcessoForm
from ....cursor import db
from ....utils.flash_errors import flash_errors
from ....tables.usuario.usuario_modelo import Usuario
from ....tables.equipe9.processo.processo_modelo import Processo
from ....utils.zelda_modelo import ZeldaModelo


class ProcessoCadastrarNegocio:

    def exibir():

        form = CadastrarProcessoForm()

        usuarios = ZeldaModelo.lista_usuarios()

        form.processo_usuario.choices = [(p.get_id(),p.login) for p in usuarios]

        if form.validate_on_submit():

            processo = Processo()

            processo.tipo = form.processo_tipo.data
            processo.descricao = form.processo_descricao.data
            processo.set_usuario( Usuario(form.processo_usuario.data) )
            processo.salva()

            return redirect(url_for('processo_listar'))

        else:
            flash_errors(form)

        return render_template('equipe9_processo_criar.html', form=form)
