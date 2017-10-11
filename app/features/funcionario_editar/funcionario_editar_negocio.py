from .funcionario_editar_form import EditarFuncionarioForm
from ...tables.funcionario.funcionario_modelo import Funcionario
from ...tables.lotacao.lotacao_modelo import Lotacao
from ...utils.flash_errors import flash_errors
from ...authentication import verifica_sessao
from ...cursor import db

import os
from werkzeug import secure_filename
from app import app, ALLOWED_EXTENSIONS
from flask import render_template, flash, redirect, url_for

class FuncionarioEditarNegocio:

    def exibir(func_id):
        form = EditarFuncionarioForm()

        func = Funcionario()
        lotacao = Lotacao()

        # Recupera todos os setores do banco
        setores = db.get_setores()

        # Adiciona dinamicamente as opções do SelectField que vai ser renderizado
        # pelo wtforms
        form.setor_id.choices = [(s.id, s.nome) for s in setores]

        # Se a página foi carregada com dados post (do formulário da própria
        # página), valida os campos
        if form.validate_on_submit():

            # Preenche um novo funcionário com os campos atualizados
            func.nome = form.funcionario_nome.data
            func.id = form.funcionario_id.data

            db.edita_funcionario(func)
            filename = secure_filename(form.file.data.filename)
            form.file.data.save(r'C:\zelda\app\funcionario\fotos\user_'+ filename)
            lotacao = db.get_lotacao_ativa(func.id)

            # Verifica se o setor selecionado permanece inalterado
            if lotacao is None or lotacao.setor_id != form.setor_id.data:

                lotacao = Lotacao()

                # Se não, cadastra uma nova lotação
                lotacao.setor_id = form.setor_id.data
                lotacao.funcionario_id = func.id

                db.cadastra_lotacao(lotacao)

            return redirect(url_for('funcionario_listar'))

        # A página pode ser acessada diretamente pela URL ao passar somente o id
        # do item a ser editado
        else:
            # Recupera o funcionário no banco
            func = db.get_funcionario(func_id)

            # Se o id encontrou algum funcionário no banco
            if func is not None:

                # Recupera a lotação ativa do funcionário no banco
                lotacao = db.get_lotacao_ativa(func_id)
                preenche_form_funcionario(form, func, lotacao)

            else:
                # Se o id é inválido, redireciona para o menu
                return redirect(url_for('funcionario_listar'))

            flash_errors(form)
            return render_template('funcionario_editar.html',form=form,setores=setores)
        return render_template('funcionario_editar.html', form=form)


def preenche_form_funcionario(form, func, lotacao):
    # Preenche o formulário com os dados atuais do funcionário

    if lotacao is not None:
        form.setor_id.default = int(lotacao.setor_id)
        form.lotacao_id.data = lotacao.id

    form.process()

    form.funcionario_nome.data = func.nome
    form.funcionario_id.data = func.id