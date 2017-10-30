from .funcionario_cadastrar_form import CadastrarFuncionarioForm
from ...tables.funcionario.funcionario_modelo import Funcionario
from ...tables.lotacao.lotacao_modelo import Lotacao
from ...utils.flash_errors import flash_errors
from ...cursor import db
from ...utils.zelda_modelo import ZeldaModelo

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
        setores = ZeldaModelo.lista_setores_ativos()

        # Adiciona dinamicamente as opções do SelectField que vai ser renderizado
        # pelo wtforms
        form.funcionario_setor_id.choices = [(s.get_id(), s.nome) for s in setores]

        funcionario = Funcionario()

        if form.validate_on_submit():
            funcionario.nome = form.funcionario_nome.data
            funcionario.salva()
            funcionario.mudar_setor(form.funcionario_setor_id.data)

            if form.file.data is not None:
                filename = secure_filename(form.file.data.filename)

                if allowed_file(filename):
                    path = os.path.abspath(os.path.join(app.config['FUNCIONARIOS_UPLOAD_PATH'], str(funcionario.get_id()) + '.' + filename.rsplit('.',1)[1]))
                    form.file.data.save(path)
                    
                    return redirect(url_for('funcionario_listar'))
                else:
                    flash("Os formatos da foto são restritos a png, jpg e jpeg")
                    
            else:
                return redirect(url_for('funcionario_listar'))
        else:
            flash_errors(form)

        return render_template('funcionario_criar.html', form=form, setores=setores)
