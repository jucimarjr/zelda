from flask_mysqldb import MySQL

class ProcessoInterfaceQuatro:

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

    def get_processos_4(self, processo_id):
        data = self.execute_query("select * from processo where processo_id = '{}' limit 1".format(processo_id))
        return data[0]


    def edita_processo_4(self,processo):
        self.execute_query("update processo set processo_desc = '{}', processo_tipo = '{}' where processo_id = '{}'".format(processo.get_desc(),processo.get_tipo(),processo.get_id()), True)

    def cadastra_processo4(self, processo):
        self.execute_query("insert into processo(processo_tipo, processo_desc, usuario_id) values('{}', '{}', '{}')".format(processo.get_tipo(), processo.get_desc(), processo.get_usuario().get_id()), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from processo")
        return data[0]["last"]

    def deleta_processos4(self, processo_id):
        self.execute_query("delete from processo where processo_id = '{}'".format(processo_id), True)
        #self.execute_query("delete from docs where processo_id = '{}'".format(processo_id), True)


    def get_processos_ids(self):
        data = self.execute_query("select processo_id from processo")
        ids = []

        if data is not None:
            for d in data:
                ids.append(d['processo_id'])

        return ids

    def edita_processos_usuario(processo):
        db.execute_query("update processo set usuario_id = '{}' where processo_id = '{}'".format(processo.get_usuario().get_id(), processo.get_id(), True))
