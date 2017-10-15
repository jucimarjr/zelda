from .usuario_signup_form import UsuarioSignupForm
from ...utils.flash_errors import flash_errors
from ...cursor import db
from flask import request
from werkzeug import secure_filename
from flask_json import json_response
from ...utils.return_errors import return_errors
class UsuarioSignupNegocio:

    def exibir(request):
        form = UsuarioSignupForm()
        #form.login.data = request.args.get('input_user')
        #form.email.data =request.args.get('input_email')
        #form.senha.data =request.args.get('input_senha')
        if form.validate_on_submit():
            if verifica_email(form.usuario_email.data):
                usuario = Usuario(login=form.usuario_login.data,senha = Criptografador.gerar_hash(form.usuario_senha.data,''),email = form.usuario_email.data,status=0)
                db.cadastra_usuario(usuario)
                return json_response(mensagem="Cadastrado")
            else:
                return json_response(mensagem="Email ja cadastrado no sistema")
        else:
            return json_response(mensagem=return_errors(form))
            
