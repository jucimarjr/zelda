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

    def get_processo(self, processo_id):
        data = self.execute_query("select * from processo where processo_id = '{}' limit 1".format(processo_id))
        return data[0]
        
    def cadastra_processo(self, processo):
        self.execute_query("insert into processo(processo_tipo, processo_id, processo_descricao, usuario_id)\
         values('{}', '{}', '{}', '{}')".format(processo.nome, processo.get_id(), processo.descricao, processo.get_usuario().get_id()), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from processo")

        if len(data) < 1:
            return None

        return data[0]["last"]

    def get_processos_usuario(self,user_id):
        data = self.execute_query("select F.* from processo as F AND P.processo_id = F.funcionalidade_id AND U.usuario_id = '{}'".format(user_id))
        return data

    def get_processos_ids(self):
        data = self.execute_query('''select processo_id from processo''')
        return data