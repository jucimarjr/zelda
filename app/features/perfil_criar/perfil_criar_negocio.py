from flask import render_template, flash, redirect, url_for
from .perfil_criar_form import CadastrarPerfilForm
from ...utils.flash_errors import flash_errors
from ...tables.perfil.perfil_modelo import Perfil
from ...tables.permissao.permissao_modelo import Permissao
from ...utils.criptografador import Criptografador
from ...cursor import db

class PerfilCadastrarNegocio:

    def exibir():
        form = CadastrarPerfilForm()

        funcionalidades = db.get_funcionalidades()
        form.funcionalidade_id.choices = [(f.funcionalidade_id, f.funcionalidade_nome) for f in funcionalidades]

        if form.validate_on_submit():

            perfil = Perfil(nome=form.perfil_nome.data)
            id = db.cadastra_perfil(perfil)

            if len(form.funcionalidade_id.data) > 0:
                for d in form.funcionalidade_id.data:
                    permissao = Permissao()
                    permissao.funcionalidade_id = d;
                    permissao.perfil_id = id
                    db.cadastra_permissao(permissao)

            return redirect(url_for('perfil_listar'))

        else:
            flash_errors(form)

        return render_template('perfil_criar.html', form=form)
