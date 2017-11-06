from .funcionario_editar_form import EditarFuncionarioForm
from ...tables.funcionario.funcionario_modelo import Funcionario
from ...utils.flash_errors import flash_errors
from ...utils.zelda_modelo import ZeldaModelo

from flask import render_template, flash, redirect, url_for

class FuncionarioEditarNegocio:

    def exibir(func_id):
        form = EditarFuncionarioForm()

        funcionario = Funcionario(func_id)

        # Recupera todos os setores do banco
        setores = ZeldaModelo.lista_setores_ativos()

        # Adiciona dinamicamente as opções do SelectField que vai ser renderizado
        # pelo wtforms
        form.setor_id.choices = [(s.get_id(), s.nome) for s in setores]

        # Se a página foi carregada com dados post (do formulário da própria
        # página), valida os campos
        if form.validate_on_submit():

            funcionario.nome = form.funcionario_nome.data
            funcionario.salva()
            funcionario.mudar_setor(form.setor_id.data)
            return redirect(url_for('funcionario_listar'))

        # A página pode ser acessada diretamente pela URL ao passar somente o id
        # do item a ser editado
        else:
            if funcionario.get_id() is None:
                return redirect(url_for('funcionario_listar'))

            flash_errors(form)

        preenche_form_funcionario(form, funcionario)
        return render_template('funcionario_editar.html', form=form)


def preenche_form_funcionario(form, func):
    # Preenche o formulário com os dados atuais do funcionário

    if func.get_setor() is not None:
        form.setor_id.default = int(func.get_setor().get_id())

    form.process()
    form.funcionario_nome.data = func.nome