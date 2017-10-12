from flask import render_template, flash, redirect, url_for
from .usuario_cadastrar_form import CadastrarUsuarioForm
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...utils.criptografador import Criptografador
from ...cursor import db

class UsuarioCadastrarNegocio:
    
    def exibir():
        form = CadastrarUsuarioForm()
        if form.validate_on_submit():
            usuario = Usuario(login=form.usuario_login.data, senha=Criptografador.gerar_hash(form.usuario_senha.data, ''), admin=form.usuario_admin.data - 1)

            db.cadastra_usuario(usuario)
            return redirect(url_for('usuario_listar'))
        else:
            flash_errors(form)
            return render_template('usuario_criar.html', form=form)