from flask_mysqldb import MySQL

class ProcessoInterfaceOito:

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

    def cadastra_processo(self, processo):
        if processo.get_usuario() is not None:
            if usuario.get_usuario().get_id() is not None:
                usuario_id = usuario.get_perfil().get_id()

        self.execute_query("insert into processo (descricao, tipo, usuario_id)\
         values ('{}', '{}', '{}')".format(processo.descricao, processo.tipo, usuario_id), True)
        data = self.execute_query('select LAST_INSERT_ID() as last from usuario')
        return data[0]['last']

    def edita_processo(self, processo):
        self.execute_query("update processo set descricao = '{}', tipo = '{}'\
         where processo_id = '{}'".format(processo.descricao, processo.tipo, processo.get_id()), True)

    def ativa_processo(self, processo_id):
        self.execute_query("update processo set situacao = 1 where processo_id = '{}'".format(processo_id), True)

    def desativa_processo(self, processo_id):
        self.execute_query("update processo set situacao = 0 where processo_id = '{}'".format(processo_id), True)

    def get_processo(id_processo):
        data = db.execute_query("SELECT * FROM processo WHERE processo_id = '{}' LIMIT 1".format(id_processo))
        return data

    def get_processos_ids():
        data = db.execute_query("select processo_id from processo")
        return data