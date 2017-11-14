from flask_mysqldb import MySQL
class ProcessoInterface:

    def __init__(self, app):
        self.mysql = MySQL(app)

    def execute_query(self, query, insert=False):
        cur = self.mysql.connection.cursor()
        cur.execute(query)

        if insert:
            self.mysql.connection.commit()
        
        data = cur.fetchall()
        cur.close()

        return data
        
    # CRUD - SETOR

    def cadastra_processo(self, processo):
        self.execute_query("insert into setor (processo_desc, processo_tipo) values (\"{}\", {})".format(processo.desc,processo_tipo), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from processo")
        return data[0]['last']


    def get_processos_ids(self):
        data = self.execute_query("select processo_id from processo")
        ids = []

        if data is not None:
            for d in data:
                ids.append(d['processo_id'])

        return ids

    def get_processos_ativos_ids(self):
        data = self.execute_query("select processo_id from processo where processo_situacao = 0")
        ids = []

        if data is not None:
            for d in data:
                ids.append(d['processo_id'])

        return ids

    def edita_processo(self, processo):
        self.execute_query("update processo set processo_desc = '{}', processo_tipo = {} where processo_id = '{}'".format(processo_desc, processo_tipo, processo.get_id()), True)

    def desativa_processo(self, processo_id):
        self.execute_query("update processo set processo_situacao = 1  where processo_id = '{}'".format(processo_id), True)

    def get_processo(self, processo_id):
        data = self.execute_query("select * from processo where processo_id = {} limit 1".format(processo_id))

        if len(data) < 1:
            return None

        return data[0]
