from flask_mysqldb import MySQL

class ProcessoInterface13:
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

     # CRUD - PROCESSO
     
    def get_processo(self,processo_id):
        data = self.execute_query("select * from processo where processo_id = '{}' limit 1".format(processo_id))
        return data[0]

    def cadastra_processo_13(self,processo):
        self.execute_query("insert into processo(processo_descricao, processso_tipo,usuario_id)\
         values('{}', '{}','{}')".format(processo.get_descricao(), processo.get_tipo(),usuario.get_usuario().get_id()), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from processo")

        if len(data) < 1:
            return None

        return data[0]["last"]
    
    def deleta_processo(self, processo_id):
        self.execute_query("delete from processo where processo_id = '{}'".format(processo_id), True)
        self.execute_query("delete from docs where processo_id = '{}'".format(processo_id), True)


    def edita_processo(self,processo):
        self.execute_query("update processo set processo_descricao = '{}', processo_tipo = '{}',usuario_id = '{}',\
         where processo_id = '{}'".format(processo.get_descricao(),processo.get_tipo(),usuario.get_usuario().get_id()), True)

    def get_processos_ids(self):
        data = self.execute_query("select processo_id from processo")
        ids = []
        if data is not None:
            for d in data:
                ids.append(d['processo_id'])

        return ids

    def edita_processo_usuario_13(processo):
        db.execute_query("UPDATE processo SET usuario_id = '{}' WHERE processo_id = '{}'".format(processo.get_usuario().get_id(), processo.get_id()), True)
