from flask_mysqldb import MySQL

class ProcessoInterfaceDois:

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

    def get_processo(self, processo_id):
        data = self.execute_query("select * from processo_dois where processo_id = {} limit 1".format(processo_id))

        if len(data) < 1:
            return None

        return data[0]


    def get_processos_ids_dois(self):
        data = self.execute_query("select * from processo_dois")
        return data

    def desativa_processo(self, processo_id):
        self.execute_query("update processo_dois set processo_status = 1  where processo_id = '{}'".format(processo_id), True)
