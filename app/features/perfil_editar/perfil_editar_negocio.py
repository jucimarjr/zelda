from flask import render_template, flash, redirect, url_for
from .perfil_editar_form import EditarPerfilForm
from ...utils.flash_errors import flash_errors
from ...tables.perfil.perfil_modelo import Perfil
from ...tables.permissao.permissao_modelo import Permissao
from ...utils.criptografador import Criptografador
from ...utils.zelda_modelo import ZeldaModelo

class PerfilEditarNegocio:

    def exibir(perfil_id):
        form = EditarPerfilForm()

        perfil = Perfil(perfil_id)
        if perfil.get_id() is None:
            return redirect(url_for('perfil_listar'))
        
        funcionalidades = ZeldaModelo.lista_funcionalidades()
        form.funcionalidades_ids.choices = [(f.get_id(), f.nome) for f in funcionalidades]
        
        if form.validate_on_submit():
            perfil.nome = form.perfil_nome.data
            perfil.salva()
            perfil.altera_funcionalidades(form.funcionalidades_ids.data)
            return redirect(url_for('perfil_listar'))
        else:
            flash_errors(form)

        form.perfil_nome.data = perfil.nome
        return render_template('perfil_editar.html', form=form)