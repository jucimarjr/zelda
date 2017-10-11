from flask import render_template, flash, redirect, url_for
from .usuario_editar_form import EditarUsuarioForm
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador
from ...cursor import db
from werkzeug import secure_filename
import os

class UsuarioEditarNegocio:
    def exibir(user_id):
        form = EditarUsuarioForm()

        usuario = Usuario()

        if form.validate_on_submit():
            usuario.login = form.usuario_login.data
            usuario.id = form.usuario_id.data
            usuario.senha = Criptografador.gerar_hash(form.usuario_senha.data, '')
            usuario.admin = form.usuario_admin.data - 1

            db.edita_usuario(usuario)
            filename = secure_filename(form.file.data.filename)
            form.file.data.save(r'C:zelda\app\usuario\fotos\user_'+filename)
            return redirect(url_for('usuario_listar'))
        else:

            usuario = db.get_usuario(user_id)

            if usuario is not None:
                form.usuario_admin.default = int(usuario.admin + 1)
                form.process()

                form.usuario_login.data = usuario.login
                form.usuario_id.data = user_id

            else:
                return redirect(url_for('usuario_listar'))

            flash_errors(form)
            return render_template('usuario_editar.html',form=form)
        return render_template('usuario_editar.html', form=form)
