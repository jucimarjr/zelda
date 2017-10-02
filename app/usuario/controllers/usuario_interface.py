from flask_mysqldb import MySQL
from ..models.usuario import Usuario

class Zelda_Usuario:

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
        self.execute_query("insert into usuario (usuario_login, usuario_senha, usuario_logado, usuario_admin) values ('{}', '{}', '{}', '{}')".format(usuario.login, usuario.senha, usuario.logado, usuario.admin), True)

    def get_usuarios(self):
        data = self.execute_query("select * from usuario")
        usuarios = []
        for u in data:
            usuario = Usuario(
                id=u["usuario_id"],
                login=u["usuario_login"],
                senha=u["usuario_senha"],
                logado=u["usuario_logado"],
                admin=u["usuario_admin"])
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
                admin=u["usuario_admin"])
            usuarios.append(usuario)
        return usuarios

    def get_usuarios_admin(self):
        data = self.execute_query("select * from usuario where usuario_admin = 1")
        usuarios = []
        for u in data:
            usuario = Usuario(
                id=u["usuario_id"],
                login=u["usuario_login"],
                senha=u["usuario_senha"],
                logado=u["usuario_logado"],
                admin=u["usuario_admin"])
            usuarios.append(usuario)
        return usuarios

    def edita_usuario(self, usuario):
        self.execute_query("update usuario set usuario_login = '{}', usuario_senha = '{}', usuario_admin = '{}' where usuario_id = '{}'".format(usuario.login, usuario.senha, usuario.admin, usuario.id), True)

    def deleta_usuario(self, usuario_id):
        self.execute_query("delete from usuario where usuario_id = '{}'".format(usuario_id), True)

    def get_usuario(self, id):
        data = self.execute_query("select * from usuario where usuario_id = '{}'".format(id))
        if len(data) < 1:
            return None
        usuarios = []
        for d in data:
            usuario = Usuario(
                id=d["usuario_id"],
                login=d["usuario_login"],
                senha=d["usuario_senha"],
                logado=d["usuario_logado"],
                admin=d["usuario_admin"])
            usuarios.append(usuario)
        return usuarios[0]

    def get_usuario_pelo_login(self, login):
        data = self.execute_query("select * from usuario where usuario_login = '{}'".format(login))
        if len(data) < 1:
            return None
        usuarios = []
        for d in data:
            usuario = Usuario(
                id=d["usuario_id"],
                login=d["usuario_login"],
                senha=d["usuario_senha"],
                logado=d["usuario_logado"],
                admin=d["usuario_admin"])
            usuarios.append(usuario)
        return usuarios[0]
