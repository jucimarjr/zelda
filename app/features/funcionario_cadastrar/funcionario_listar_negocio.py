from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from funcionario_listar_form import CadastrarFuncionarioForm
from ...funcionario2.funcionario_modelo import Funcionario
from ...funcionario2.funcionario_interface import FuncionarioInterface
from ..flash_errors.flash_errors_negocio import FlashErrorsNegocio
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_mysqldb import MySQL

class FuncionarioCadastrarNegocio:

    def exibir(db):
        if(session['user_login'] == ""):
            return redirect(url_for('index'))

        form = CadastrarFuncionarioForm()

        # Recupera todos os setores do banco
        setores = db.get_setores_ativos()

        # Adiciona dinamicamente as opções do SelectField que vai ser renderizado
        # pelo wtforms
        form.funcionario_setor_id.choices = [(s.id, s.nome) for s in setores]
        form.funcionario_setor_id.default = 1  # O setor de id 1 no banco é o Nenhum

        if form.validate_on_submit():
            funcionario = Funcionario(nome=form.funcionario_nome.data)

            db.cadastra_funcionario(funcionario)
            funcionarios = db.get_funcionarios()

            lotacao = Lotacao(funcionario_id=len(funcionarios), setor_id=form.funcionario_setor_id.data)

            db.cadastra_lotacao(lotacao)
            return redirect(url_for('funcionario_listar'))
        else:
            FlashErrorsNegocio.flash_errors(form)
            return render_template('funcionario_criar.html', form=form, setores=setores)