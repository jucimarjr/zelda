from flask_mysqldb import MySQL

class ProcessosInterfaceDoze:

    def __init__(self,app):
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

    def get_processos_ids(self):
        data = self.execute_query("select processo_id from processo")
        return data

    def get_processo_12(self, processo_id):
        data = self.execute_query("select * from processo where processo_id ='{}'limit 1".format(processo_id))
        if len(data)<1:
            return None
        return data[0]

    def cadastra_processo(self,processo):
        self.execute_query("insert into processo(processo_tipo,processo_desc) values('{}','{}')".format(processo.tipo, processo.desc), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from processo")
        return data[0]['last']

    def edita_processo_12(self, processo):
        self.execute_query("update processo set processo_tipo='{}',processo_desc='{}' where processo_id='{}'".format(processo.tipo,processo.desc, processo.get_id_12()),True)

    def deleta_processo(self,processo):
        self.execute_query("delete from usuario where usuario_id='{}'".format(processo_id),True)
