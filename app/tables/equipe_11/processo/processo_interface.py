from flask_mysqldb import MySQL

class ProcessoInterfaceOnze:
    def init(self, app):
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
        data = self.execute_query("select * from processo where processo_id = '{}'".format(processo_id['processo_id']))
        return data[0]

    def cadastra_processo(self, processo):
        self.execute_query("insert into processo(processo_tipo, processo_desc, processo_status) values(\"{}\", '{}', '{}')".format(processo.processo_tipo, processo.processo_desc, 0), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from processo")

        if len(data) < 1:
            return None

        return data[0]["last"]

    def get_processos_usuario(self,user_id):
        data = self.execute_query("select F.* from processo as F, permissao as P, usuario as U where P.perfil_id = U.perfil_id AND P.processo_id = F.processo_id AND U.usuario_id = '{}'".format(user_id))
        return data

    def get_processos_ids(self):
        data = self.execute_query('''select processo_id from processo''')
        return data

    def edita_processo(self, processo):
        self.execute_query("update processo set processo_tipo = '{}', processo_desc = '{}' where processo_id = '{}'".format(processo.processo_tipo, processo.processo_desc, processo.get_id()['processo_id']), True)

    def get_usuario(self):
        data = self.execute_query("select usuario_id from usuario")
        return data

    def desativa_processo(self, processo_id):
        self.execute_query("update processo set processo_status = 1 where processo_id = \"{}\"".format(processo_id['processo_id']), True)
