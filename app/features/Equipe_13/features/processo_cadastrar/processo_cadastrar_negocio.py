from flask import render_template, redirect, url_for
from .processo_cadastrar_form import ProcessoCadastrarForm
from .....utils.zelda_modelo import ZeldaModelo
from ..features.Equipe_13.tables.processo.processo_modelo import Processo
from .....utils.flash_errors import flash_errors
from .....tables.usuario.usuario_modelo import Usuario

class ProcessoCadastrarNegocio:
    def exibir():
        form = ProcessoCadastrarForm()

        usuarios = ZeldaModelo.lista_usuarios()
        form.usuario.choices = [ (usuario.get_id(), usuario.login) for usuario in usuarios ]
        form.tipo.choices = [ (index, Processo.lista_tipos[index]) for index in range(0, len(Processo.lista_tipos))]
        form.tipo.default = 0

        if form.validate_on_submit():
            processo = Processo(usuario = Usuario(form.usuario.data))
            processo.descricao = form.descricao.data
            processo.tipo = form.tipo.data
            processo.salva()

            return redirect(url_for('processo_listar_13'))
        else:
            flash_errors(form)

        return render_template('processo_criar_13.html', form = form)
