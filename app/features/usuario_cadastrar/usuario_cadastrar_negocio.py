from flask import render_template, flash, redirect, url_for
from .usuario_cadastrar_form import CadastrarUsuarioForm
from ...cursor import db
from ...utils.flash_errors import flash_errors
from ...tables.usuario.usuario_modelo import Usuario
from ...tables.perfil.perfil_modelo import Perfil
from ...utils.criptografador import Criptografador
from ...utils.zelda_modelo import ZeldaModelo
from ...utils.files import flash_errors_extensao
from flask_json import json_response

class UsuarioCadastrarNegocio:

    def exibir():

        form = CadastrarUsuarioForm()

        perfis = ZeldaModelo.lista_perfis()

        form.usuario_perfil.choices = [(p.get_id(),p.nome) for p in perfis]

        if form.validate_on_submit():

            data = db.verifica_existe_email(form.usuario_email.data)

            if len(data) > 0:
                flash("Email já cadastrado no sistema.")
                return render_template('usuario_criar.html', form=form)

            usuario = Usuario()

            usuario.login = form.usuario_login.data
            usuario.email = form.usuario_email.data
            usuario.set_perfil( Perfil(form.usuario_perfil.data) )
            usuario.salva()

            usuario.set_senha(form.usuario_senha.data)

            usuario.ativa()

            if form.file.data is not None:
                usuario.set_foto(form.file.data)
                if usuario.get_caminho_foto() is None:
                    flash_errors_extensao()
                    return render_template('usuario_criar.html', form=form)

            return redirect(url_for('usuario_listar'))

        else:
            flash_errors(form)

        return render_template('usuario_criar.html', form=form)
