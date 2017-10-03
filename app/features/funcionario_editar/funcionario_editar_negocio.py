from funcionario_editar_form import EditarFuncionarioForm
from ...funcionario2.funcionario_modelo import Funcionario
from ...funcionario2.funcionario_interface import FuncionarioInterface
from ...lotacao2.lotacao_modelo import Lotacao
from flash_errors_negocio import FlashErrorsNegocio
from preenche_dados_negocio import PreencheDadosNegocio
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

class FuncionarioEditarNegocio():

    def exibir(func_id):
        if(session['user_login'] == ""):
            return redirect(url_for('index'))

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
                PreencheDadosNegocio.preenche_dados_atuais(form, func, lotacao)

            else:
                # Se o id é inválido, redireciona para o menu
                return redirect(url_for('funcionario_listar'))

            flash_errors(form)

        return render_template('funcionario_editar.html', form=form)