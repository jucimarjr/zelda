from .funcionario_cadastrar_form import CadastrarFuncionarioForm
from ...tables.funcionario.funcionario_modelo import Funcionario
from ...tables.lotacao.lotacao_modelo import Lotacao
from ...utils.flash_errors import flash_errors
from ...authentication import verifica_sessao
from ...cursor import db

import os
from werkzeug import secure_filename
from app import app, ALLOWED_EXTENSIONS
from flask import render_template, flash, redirect, url_for

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class FuncionarioCadastrarNegocio:

    def exibir():
        form = CadastrarFuncionarioForm()

        # Recupera todos os setores do banco
        setores = db.get_setores_ativos()

        # Adiciona dinamicamente as opções do SelectField que vai ser renderizado
        # pelo wtforms
        form.funcionario_setor_id.choices = [(s.id, s.nome) for s in setores]
        form.funcionario_setor_id.default = 1  # O setor de id 1 no banco é o Nenhum

        if form.validate_on_submit():
            funcionario = Funcionario(nome=form.funcionario_nome.data)

            id = db.cadastra_funcionario(funcionario)

            lotacao = Lotacao(funcionario_id=id, setor_id=form.funcionario_setor_id.data)

            db.cadastra_lotacao(lotacao)

            filename = secure_filename(form.file.data.filename)

            if allowed_file(filename):
                path = os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], str(id) + '.' + filename.rsplit('.',1)[1]))
                form.file.data.save(path)
                
                return redirect(url_for('funcionario_listar'))
            else:
                flash("Os formatos da foto são restritos a png, jpg e jpeg")
        else:
            flash_errors(form)

        return render_template('funcionario_criar.html', form=form, setores=setores)
