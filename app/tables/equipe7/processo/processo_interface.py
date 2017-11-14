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

    # CRUD - PERFIL

    def cadastra_processo(self, processo):
        self.execute_query("insert into processo (processo_tipo, processo_desc) values ('{}','{}')".format(processo.tipo, processo.desc), True)
        data = self.execute_query("select processo_id from processo order by processo_id desc limit 1")

        return data[0]["processo_id"]

    def edita_processo(self, processo):
        self.execute_query("update processo set processo_tipo = '{}', processo_desc = '{}' where processo_id = '{}'".format(processo.tipo, processo.desc, processo.get_id()), True)

    def deleta_processo(self, processo_id):
        self.execute_query("delete from processo where processo_id = '{}'".format(processo_id), True)

    def get_processo(self, processo_id):
        data = self.execute_query("select * from processo where processo_id = '{}'".format(processo_id))
        return data

    def get_processo_ids(self):
        data = self.execute_query("select processo_id from processo")
        return data