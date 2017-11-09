from .funcionario_cadastrar_form import CadastrarFuncionarioForm
from ...tables.funcionario.funcionario_modelo import Funcionario
from ...tables.lotacao.lotacao_modelo import Lotacao
from ...utils.flash_errors import flash_errors
from ...cursor import db
from ...utils.zelda_modelo import ZeldaModelo
from flask import render_template, flash, redirect, url_for
class FuncionarioCadastrarNegocio:

    def exibir():
        form = CadastrarFuncionarioForm()

        # Recupera todos os setores do banco
        setores = ZeldaModelo.lista_setores_ativos()

        # Adiciona dinamicamente as opções do SelectField que vai ser renderizado
        # pelo wtforms
        form.funcionario_setor_id.choices = [(s.get_id(), s.nome) for s in setores]

        funcionario = Funcionario()

        if form.validate_on_submit():
            funcionario.nome = form.funcionario_nome.data
            funcionario.salva()
            funcionario.mudar_setor(form.funcionario_setor_id.data)
            return redirect(url_for('funcionario_listar'))
        else:
            flash_errors(form)

        return render_template('funcionario_criar.html', form=form, setores=setores)
