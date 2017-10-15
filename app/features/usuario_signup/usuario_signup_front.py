import json
from app import app
from flask_json import json_response
from .usuario_signup_negocio import UsuarioSignupNegocio
from flask import request


app.config['JSON_ADD_STATUS'] = False

@app.route('/cadastrar',methods=['POST'])
def cadastrar():
    return UsuarioSignupNegocio.exibir(request)
