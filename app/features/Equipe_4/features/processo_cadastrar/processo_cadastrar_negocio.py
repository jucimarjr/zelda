from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import CadastrarProcessoForm
from app.cursor import db
from app.utils.flash_errors import flash_errors
from app.tables.equipe4.tables.processo.processo_modelo import Processo
from app.utils.zelda_modelo import ZeldaModelo
from app.tables.usuario.usuario_modelo import Usuario


class ProcessoCadastrarNegocio:

    def exibir():

        form = CadastrarProcessoForm()
        usuarios = ZeldaModelo.lista_usuarios()
        form.usuario.choices = [ (usuario.get_id(), usuario.login) for usuario in usuarios ]
        
        if form.validate_on_submit():
            processo = Processo()

            processo.set_usuario(usuario = Usuario(form.usuario.data))
            processo.tipo = form.processo_tipo.data
            processo.desc = form.processo_desc.data
            processo.salva()

            return redirect(url_for('processo_listar_4'))

        else:
            flash_errors(form)

        return render_template('equipe4_processo_criar.html', form=form)
