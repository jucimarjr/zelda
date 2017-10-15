from flask_mysqldb import MySQL
from .usuario_modelo import Usuario

class UsuarioInterface:

    def __init__(self, app):
        self.mysql = MySQL(app)

    def execute_query(self, query, insert=False):
        cur = self.mysql.connection.cursor()
        cur.execute(query)
        if insert:
            self.mysql.connection.commit()
        else:
            data = cur.fetchall()
            cur.close()
        return data

 # CRUD - USUARIO
    def cadastra_usuario(self, usuario):
        self.execute_query("insert into usuario (usuario_login, usuario_senha, usuario_logado, perfil_id) values ('{}', '{}', '{}', '{}')".format(usuario.login, usuario.senha, usuario.logado, usuario.perfil_id), True)

    def get_usuarios(self):
        data = self.execute_query("select * from usuario")
        usuarios = []
        for u in data:
            usuario = Usuario(
                id=u["usuario_id"],
                login=u["usuario_login"],
                senha=u["usuario_senha"],
                logado=u["usuario_logado"],
                #email=u["usuario_email"],
                #confirmaemail=u["usuario_confirmaemail"],
                perfil_id=u["perfil_id"])
            usuarios.append(usuario)
        return usuarios

    def get_usuarios_logados(self):
        data = self.execute_query("select * from usuario\
            where usuario_logado = 1")
        usuarios = []
        for u in data:
            usuario = Usuario(
                id=u["usuario_id"],
                login=u["usuario_login"],
                senha=u["usuario_senha"],
                logado=u["usuario_logado"],
                #email=u["usuario_email"],
                #confirmaemail=u["usuario_confirmaemail"],
                perfil_id=u["perfil_id"])
            usuarios.append(usuario)
        return usuarios

    def get_usuarios_admin(self):
        setor_admin_id = self.execute_query("select perfil_id from perfil where perfil_nome = {}".format("Administrador"))
        data = self.execute_query("select * from usuario where perfil_id = {}".format(setor_admin_id[0]))
        usuarios = []
        for u in data:
            usuario = Usuario(
                id=u["usuario_id"],
                login=u["usuario_login"],
                senha=u["usuario_senha"],
                logado=u["usuario_logado"],
                #email=u["usuario_email"],
                #confirmaemail=u["usuario_confirmaemail"],
                perfil_id=u["perfil_id"])
            usuarios.append(usuario)
        return usuarios

    def get_usuarios_by_perfil(self, id):
        data = self.execute_query("select * from usuario where perfil_id = {}".format(id))
        usuarios = []
        for d in data:
            usuario = Usuario(
                id=u["usuario_id"],
                login=u["usuario_login"],
                senha=u["usuario_senha"],
                logado=u["usuario_logado"],
                #email=u["usuario_email"],
                #confirmaemail=u["usuario_confirmaemail"],
                perfil_id=u["perfil_id"])
            usuarios.append(usuario)
        return usuarios

    def edita_usuario(self, usuario):
        self.execute_query("update usuario set usuario_login = '{}', usuario_senha = '{}', perfil_id = '{}' where usuario_id = '{}'".format(usuario.login, usuario.senha, usuario.perfil_id, usuario.id), True)

    def deleta_usuario(self, usuario_id):
        self.execute_query("delete from usuario where usuario_id = '{}'".format(usuario_id), True)

    def get_usuario(self, id):
        data = self.execute_query("select * from usuario where usuario_id = '{}'".format(id))
        if len(data) < 1:
            return None
        usuarios = []
        for d in data:
            usuario = Usuario(
                id=u["usuario_id"],
                login=u["usuario_login"],
                senha=u["usuario_senha"],
                logado=u["usuario_logado"],
                #email=u["usuario_email"],
                #confirmaemail=u["usuario_confirmaemail"],
                perfil_id=u["perfil_id"])
            usuarios.append(usuario)
        return usuarios[0]

    def get_usuario_pelo_login(self, login):
        data = self.execute_query("select * from usuario where usuario_login = '{}'".format(login))
        if len(data) < 1:
            return None
        usuarios = []
        for d in data:
            usuario = Usuario(
                id=u["usuario_id"],
                login=u["usuario_login"],
                senha=u["usuario_senha"],
                logado=u["usuario_logado"],
                #email=u["usuario_email"],
                #confirmaemail=u["usuario_confirmaemail"],
                perfil_id=u["perfil_id"])
            usuarios.append(usuario)
        return usuarios[0]
