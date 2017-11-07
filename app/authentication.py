from flask import session
from .utils.criptografador import Criptografador
from .cursor import db
from app import app
from .tables.usuario.usuario_modelo import Usuario
from datetime import timedelta

def inicia_sessao(user_id):
    session['user_id'] = user_id
    session.permanent = True

def encerra_sessao():
    session.pop('user_id', None)

def autentica(login, senha):
    senhaHash = Criptografador.gerar_hash(senha, '')

    result = db.verifica_credenciais(login = login, senha = senhaHash)

    if result is not None:
        inicia_sessao(result)
        return True

    return False

def sessao_ativa():
    if 'user_id' not in session:
        return False

    if retorna_usuario() is None:
        return False

    return True

def retorna_usuario():
    usuario = Usuario(session['user_id'])

    if usuario.get_id() is None:
        return None

    return usuario

def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)

def sessao_expirada():
    if session.permanent is False:
        return True
    return False