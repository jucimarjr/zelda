from flask  import session
from .classes import Criptografador
from .db_interface import Zelda

'''from app import app
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mps2017'
app.config['MYSQL_DB'] = 'zelda'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
db = Zelda(app)'''

#session['user_login'] = ''

def inicia_sessao(user_login):
    session['user_login'] = user_login

def encerra_sessao():
    session.pop('username', None)
    session['user_login'] = ''

def autentica(user_senha, db):
    senhaHash = Criptografador.gerar_hash(user_senha, '')

    autenticado = db.verifica_login(login=session['user_login'], senha=senhaHash)
    if autenticado:
        return True
    else:
        return False

def is_logado(db):
    return db.verifica_logado(login=session['user_login'])

def is_admin(db):
    return db.verifica_admin(login=session['user_login'])

def set_logado(value, db):
    if (value):
        db.set_logado_true
    else:
        db.set_logado_false

def verifica_sessao():
    if (session['user_login'] == ''):
        return True
    return False

def retorna_usuario():
    return session['user_login']
