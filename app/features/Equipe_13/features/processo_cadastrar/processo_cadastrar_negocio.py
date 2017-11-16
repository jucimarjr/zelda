
from flask import render_template, flash, redirect, url_for
from .processo_cadastrar_form import ProcessoCadastrarForm
from .....cursor import db
from .....utils.flash_errors import flash_errors
from .....utils.zelda_modelo import ZeldaModelo
from ...tables.processo.processo_modelo import Processo
from .....utils.zelda_modelo_13 import ProcessoModelo
from .....tables.usuario.usuario_modelo import Usuario


class ProcessoCadastrarNegocio:

    def exibir():

        form = ProcessoCadastrarForm()
        usuarios = ZeldaModelo.lista_usuarios()
        form.usuario.choices = [ (usuario.get_id(), usuario.login) for usuario in usuarios ]

        if form.validate_on_submit():
            
            processo = Processo(usuario = Usuario(form.usuario.data))
            processo.tipo = form.processo_tipo.data
            processo.descricao = form.processo_descricao.data
            processo.salva()

            #return redirect(url_for('processo_'))

        else:
            flash_errors(form)

        return render_template('processo_criar_13.html', form=form)
