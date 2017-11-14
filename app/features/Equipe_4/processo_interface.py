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
        

    def edita_processo(self,processo):
        self.execute_query("update processo set processo_desc = '{}', processo_tipo = '{}',usuario_id = '{}',\
         where processo_id = '{}'".format(processo.get_desc,processo.get_tipo(),usuario.get_usuario().get_id()), True)

    def cadastra_processo(self, processo):
        self.execute_query("insert into processo(processo_tipo, processo_desc, usuario_id)\
         values('{}', '{}', '{}', '{}')".format(processo.get_tipo(), processo.get_desc(), processo.get_usuario().get_id()), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from processo")

        if len(data) < 1:
            return None

        return data[0]["last"]

    def deleta_processo():
        self.execute_query("delete from processo where processo_id = '{}'".format(processo_id), True)
        self.execute_query("delete from docs where processo_id = '{}'".format(processo_id), True)    

    
    def get_processos_ids(self):
        data = self.execute_query("select processo_id from setor")
        ids = []

        if data is not None:
            for d in data:
                ids.append(d['processo_id'])

        return ids

    #Talvez não tenha
    def get_processos_usuario(self,user_id):
        data = self.execute_query("select F.* from processo as F AND P.processo_id = F.funcionalidade_id AND U.usuario_id = '{}'".format(user_id))
        return data

    
