from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import CadastrarProcessoForm
from ....cursor import db
from ....utils.flash_errors import flash_errors
from ....tables.equipe7.processo.processo_modelo import Processo
from ....tables.usuario.usuario_modelo import Usuario
from ....utils.zelda_modelo import ZeldaModelo

class ProcessoCadastrarNegocio:

    def exibir():

        form = CadastrarProcessoForm()

        usuarios = ZeldaModelo.lista_usuarios()

        form.processo_usuario.choices = [(p.get_id(),p.login) for p in usuarios]
        if form.validate_on_submit():

            processo = Processo()

            processo.set_usuario(Usuario(form.processo_usuario.data))
            processo.tipo = form.processo_tipo.data
            processo.descricao = form.processo_desc.data
            processo.salva()

            return redirect(url_for('processo_listar'))

        else:
            flash_errors(form)

        return render_template('equipe7_processo_criar.html', form=form)
