from app import app, mail, SERVER_URL
from config import ADMINS
from flask_mail import Message
from flask import url_for, flash
from itsdangerous import URLSafeTimedSerializer

class Mailer():
    def __init__(self, titulo, sender, destinatarios):
         self.__msg = Message(titulo, sender = sender, recipients = destinatarios)

    def set_body(self, body):
        self.__msg.body = body

    def set_id_registro(self, id_registro):
        self.__id_registro = id_registro
        self.__token = gerar_token(id_registro)

    def enviar(self):
        with app.app_context():
            try:
                mail.send(self.__msg)
                return True
            except:
                return False

    def get_token(self):
        return self.__token

def enviar_email_confirmacao(usuario):
    destinatarios = [ usuario.email ]
    remetente = ADMINS[0]

    mailer = Mailer('Zelda - Confirmação de email', remetente, destinatarios)
    mailer.set_id_registro(usuario.get_id())

    link = SERVER_URL + url_for('confirmar_email', token = mailer.get_token(), external = True)
    corpo = 'Bem vindo! Clique no link a seguir para confirmar seu endereço de email: {}'.format(link)

    mailer.set_body(corpo)
    if mailer.enviar():
        flash('Um email foi enviado para o endereço ' + usuario.email + '. Acesse-o para ativar sua conta.')
    else:
        flash('Houve um erro ao tentar enviar o email, tente novamente')

def enviar_email_recuperacao(usuario):
    destinatarios = [ usuario.email ]
    remetente = ADMINS[0]

    mailer = Mailer('Zelda - Recuperação de senha', remetente, destinatarios)
    mailer.set_id_registro(usuario.get_id())

    link = SERVER_URL + url_for('recuperar_senha', token = mailer.get_token(), external = True)
    corpo = 'Bem vindo! Clique no link a seguir para trocar sua senha: {}'.format(link)

    mailer.set_body(corpo)
    if mailer.enviar():
        flash('Um email foi enviado para o endereço ' + usuario.email + '. Acesse-o para trocar sua senha.')
    else:
        flash('Houve um erro ao tentar enviar o email, tente novamente')


def gerar_token(id_registro):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    token = s.dumps(id_registro, salt = app.config['SALT'])
    return token
    
def extrair_token(token):
    try:
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        id_registro = s.loads(token, salt= app.config['SALT'], max_age=3600)
    except:
        return None
    
    return id_registro