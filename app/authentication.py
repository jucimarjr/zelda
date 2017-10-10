from flask  import session
from .utils.criptografador import Criptografador
from .db_interface import Zelda
from .cursor import db

#session['user_login'] = ''

def inicia_sessao(user_login):
    session['user_login'] = user_login

def encerra_sessao():
    session.pop('username', None)
    session['user_login'] = ''

def autentica(user_senha):
    senhaHash = Criptografador.gerar_hash(user_senha, '')

    autenticado = db.verifica_login(login=session['user_login'], senha=senhaHash)
    if autenticado:
        return True
    else:
        return False

def is_logado():
    return db.verifica_logado(login=session['user_login'])

def is_admin():
    return db.verifica_admin(login=session['user_login'])

def set_logado(value):
    if (value):
        db.set_logado_true
    else:
        db.set_logado_false

def verifica_sessao():
    if 'user_login' in session:
        if (session['user_login'] == ''):
            return True
    else:
        return True
    return False

def retorna_usuario():
    return db.get_usuario_pelo_login(login=session['user_login'])
