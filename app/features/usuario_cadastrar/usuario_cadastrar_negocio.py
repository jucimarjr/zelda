from flask import render_template, flash, redirect, url_for
from .usuario_cadastrar_form import CadastrarUsuarioForm
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador
from ...cursor import db
import os

from werkzeug import secure_filename
from app import app, ALLOWED_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UsuarioCadastrarNegocio:
    
    def exibir():

        form = CadastrarUsuarioForm()
        
        perfils = db.get_perfil()

        form.usuario_perfil.choices = [(p.id,p.nome) for p in perfils]
        form.usuario_perfil.default = 1


        
        if form.validate_on_submit():
            usuario = Usuario(login=form.usuario_login.data, senha=Criptografador.gerar_hash(form.usuario_senha.data, ''), perfil_id=form.usuario_perfil.data )

            db.cadastra_usuario(usuario)
            
            if form.file.data is not None:
                filename = secure_filename(form.file.data.filename)

                if allowed_file(filename):
                    path = os.path.abspath(os.path.join(app.config['USUARIOS_UPLOAD_PATH'], str(user_id) + '.' + filename.rsplit('.',1)[1]))
                    form.file.data.save(path)
                    return redirect(url_for('usuario_listar'))
                else:
                    flash("Os formatos da foto são restritos a png, jpg e jpeg")

            else:
                return redirect(url_for('usuario_listar'))
            
            return redirect(url_for('usuario_listar'))
        
        else:
            flash_errors(form)
        
        return render_template('usuario_criar.html', form=form)
