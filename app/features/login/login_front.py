from .login_negocio import LoginNegocio
from app import app
from flask import redirect, url_for
from ...authentication import verifica_sessao

@app.route('/login', methods=['GET','POST'])
def login():
    if verifica_sessao() is False:
        return redirect(url_for('home'))
    return LoginNegocio.exibir()