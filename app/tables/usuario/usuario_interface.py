from flask_mysqldb import MySQL

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

    def cadastra_usuario(self, usuario):
        perfil = 2
        if usuario.get_perfil() is not None:
            if usuario.get_perfil().get_id() is not None:
                perfil = usuario.get_perfil().get_id()

        self.execute_query("insert into usuario (usuario_login, usuario_email, usuario_senha, usuario_caminho_foto, perfil_id)\
         values ('{}', '{}', '{}', '{}', '{}')".format(usuario.login, usuario.email, usuario.senha, usuario.caminho_foto, perfil), True)
        data = self.execute_query('select LAST_INSERT_ID() as last from usuario')
        return data[0]['last']

    def get_usuarios_ids(self):
        data = self.execute_query("select usuario_id from usuario")
        return data

    def ativa_usuario(self, usuario_id):
        self.execute_query("update usuario set usuario_status = 1 where usuario_id = '{}'".format(usuario_id), True)

    def edita_usuario(self, usuario):
        perfil = '2'
        if usuario.get_perfil() is not None:
            if usuario.get_perfil().get_id() is not None:
                perfil = usuario.get_perfil().get_id()

        self.execute_query("update usuario set usuario_login = '{}', usuario_senha = '{}', usuario_email = '{}', usuario_caminho_foto = '{}', perfil_id = {}\
         where usuario_id = '{}'".format(usuario.login, usuario.senha, usuario.email, usuario.caminho_foto, perfil, usuario.get_id()), True)

    def deleta_usuario(self, usuario_id):
        self.execute_query("delete from usuario where usuario_id = '{}'".format(usuario_id), True)

    def get_usuario(self, id):
        data = self.execute_query("select usuario_id, usuario_login, usuario_senha, usuario_logado, usuario_email, usuario_status,\
         usuario_caminho_foto, perfil_id from usuario where usuario_id = '{}' limit 1".format(id))
        return data

    def verifica_credenciais(self, login, senha):
        data = self.execute_query("select usuario_id from usuario where usuario_login = '{}' and usuario_senha = '{}'".format(login, senha))
        if len(data) < 1:
            return None

        return data[0]['usuario_id']
