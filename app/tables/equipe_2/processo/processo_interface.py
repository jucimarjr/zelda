from flask_mysqldb import MySQL

class ProcessoInterface:

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

    def get_processos_ids(self, usuario_id):
        data = self.execute_query("select processo_id from processo where usuario_id = '{}'".format(usuario_id))
        ids = []

        if data is not None:
            for d in data:
                ids.append(d['processo_id'])

        return ids