from flask_mysqldb import MySQL

class DocumentoInterface:
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

    def get_documento(self, documento_id):
        data = self.execute_query("select * from documento where documento_id = '{}' limit 1".format(documento_id))
        return data[0]
        
        def cadastra_documento(self, documento):
            self.execute_query("insert into documento(documento_desc, processo_id)\
                values('{}', '{}')".format(documento.desc, documento.get_sistema().get_id()), True)
            data = self.execute_query("select LAST_INSERT_ID() as last from documento")

        if len(data) < 1:
            return None

        return data[0]["last"]

    '''def get_funcionalidades_usuario(self,user_id):
        data = self.execute_query("select F.* from funcionalidade as F, permissao as P, usuario as U where P.perfil_id = U.perfil_id AND P.funcionalidade_id = F.funcionalidade_id AND U.usuario_id = '{}'".format(user_id))
        return data'''

    def get_documentos_ids(self):
        data = self.execute_query('''select documento_id from documento''')
        return data

    def edita_documento(self, documento):
        self.execute_query("update documento set documento_desc = '{}',processo_id = '{}'\
                           where documento_id = '{}'".format(documento.desc,documento.get_processo().get_id(),documento.get_id()),True)

        
        def desativa_documento(self, documento_id):
            self.execute_query("update documento set documento_status = 1 where documento_id = '{}'".format(documento_id), True)
