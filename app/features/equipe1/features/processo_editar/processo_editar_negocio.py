from flask import render_template, redirect, url_for
from .processo_editar_form import ProcessoEditarForm
from .....utils.zelda_modelo import ZeldaModelo
from ...tables.processo.processo_modelo import Processo
from .....utils.flash_errors import flash_errors
from .....tables.usuario.usuario_modelo import Usuario

class ProcessoEditarNegocio:
    def exibir(processo_id):
        form = ProcessoEditarForm()

        processo = Processo(processo_id)
        if processo.get_id() is None:
            return redirect(url_for('equipe1_processo_listar'))

        form.tipo.choices = [ (index, Processo.lista_tipos[index]) for index in range(0, len(Processo.lista_tipos))]
        form.tipo.default = processo.tipo
        form.descricao.data = processo.descricao

        if form.validate_on_submit():
            processo.descricao = form.descricao.data
            processo.tipo = form.tipo.data
            processo.salva()

            return redirect(url_for('equipe1_processo_listar'))
        else:
            flash_errors(form)

        return render_template('equipe1_processo_editar.html', form = form, processo = processo)