from flask_mysqldb import MySQL

class ProcessoInterface7:

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
        usuario = 2
        if processo.get_usuario() is not None:
            if processo.get_usuario().get_id() is not None:
                usuario = processo.get_usuario().get_id()

        self.execute_query("insert into processo (usuario_id, descricao, tipo)\
         values ('{}', '{}', '{}')".format(usuario, processo.descricao, processo.tipo), True)
        data = self.execute_query('select LAST_INSERT_ID() as ultimo from processo')
        return data[0]['ultimo']

    def edita_processo(self, processo):
        usuario = '2'
        if processo.get_usuario() is not None:
            if processo.get_usuario().get_id() is not None:
                usuario = processo.get_usuario().get_id()

        self.execute_query("update processo set usuario_id = '{}', descricao = '{}', tipo = {}\
         where processo_id = '{}'".format(usuario, processo.desc, processo.tipo, processo.get_id()), True)

    def deleta_processo(self, processo_id):
        self.execute_query("delete from processo where processo_id = '{}'".format(processo_id), True)

    def get_processo(self, processo_id):
        data = self.execute_query("select * from processo where processo_id = '{}'".format(processo_id))
        return data

    def get_processo_ids(self):
        data = self.execute_query("select processo_id from processo")
        return data