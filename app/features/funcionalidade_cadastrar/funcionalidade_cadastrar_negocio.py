from .funcionalidade_cadastrar_form import CadastrarFuncionalidadeForm
from ...tables.funcionalidade.funcionalidade_modelo import Funcionalidade
from ...utils.flash_errors import flash_errors
from ...cursor import db

import os
from werkzeug import secure_filename
from app import app, ALLOWED_EXTENSIONS
from flask import render_template, flash, redirect, url_for

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class FuncionalidadeCadastrarNegocio:

    def exibir():
        form = CadastrarFuncionalidadeForm()

        funcionalidade = Funcionalidade()

        if form.validate_on_submit():
            
            funcionalidade.nome = form.funcionalidade_nome.data
            funcionalidade.codigo = form.funcionalidade_codigo.data
            funcionalidade.desc = form.funcionalidade_desc.data
            
            db.cadastra_funcionalidade(funcionalidade)
        
            if form.file.data is not None:
                filename = secure_filename(form.file.data.filename)

                if allowed_file(filename):
                    path = os.path.abspath(os.path.join(app.config['FUNCIONALIDADES_UPLOAD_PATH'], str(id) + '.' + filename.rsplit('.',1)[1]))
                    form.file.data.save(path)
                    
                    return redirect(url_for('funcionalidade_listar'))
                else:
                    flash("Os formatos da foto são restritos a png, jpg e jpeg")
                    
            else:
                return redirect(url_for('funcionalidade_listar'))
            return redirect(url_for('funcionalidade_listar'))
        else:
            flash_errors(form)

        return render_template('funcionalidade_criar.html', form=form)
