from flask import render_template, flash, redirect, url_for
from .usuario_cadastrar_form import CadastrarUsuarioForm
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...tables.perfil.perfil_modelo import Perfil
from ...utils.criptografador import Criptografador
from ...utils.zelda_modelo import ZeldaModelo
import os

from werkzeug import secure_filename
from app import app, ALLOWED_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UsuarioCadastrarNegocio:
    
    def exibir():

        form = CadastrarUsuarioForm()
        
        perfis = ZeldaModelo.lista_perfis()

        form.usuario_perfil.choices = [(p.get_id(),p.nome) for p in perfis]
        
        if form.validate_on_submit():
            usuario = Usuario()

            usuario.login = form.usuario_login.data
            usuario.senha = Criptografador.gerar_hash(form.usuario_senha.data, '')
            usuario.set_perfil( Perfil(form.usuario_perfil.data) )
            
            caminho_foto = None
            if form.file.data is not None:
                usuario.salva()
                filename = secure_filename(form.file.data.filename)

                if allowed_file(filename):
                    usuario.caminho_foto = str(usuario.get_id()) + '.' + filename.rsplit('.',1)[1]
                    path = os.path.abspath(os.path.join(app.config['USUARIOS_UPLOAD_PATH'], usuario.caminho_foto))
                    
                    form.file.data.save(path)
                else:
                    flash("Os formatos da foto são restritos a png, jpg e jpeg")
                    return render_template('usuario_cadastrar.html', form = form)

            usuario.salva()

            return redirect(url_for('usuario_listar'))

        else:
            flash_errors(form)

        return render_template('usuario_criar.html', form=form)
