from flask_mysqldb import MySQL

class DocumentoInterfaceOnze:
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

    def get_documento(self, documento_id):
        try:
            data = self.execute_query("select * from documento where documento_id = '{}'".format(documento_id['documento_id']))
        except TypeError:
            data = self.execute_query("select * from documento where documento_id = '{}'".format(documento_id))
        return data[0]

    def cadastra_documento(self, documento):
        self.execute_query("insert into documento(documento_tipo, documento_desc) values(\"{}\", '{}')".format(documento.documento_tipo, documento.documento_desc), True)
        data = self.execute_query("select LAST_INSERT_ID() as last from documento")

        if len(data) < 1:
            return None

        return data[0]["last"]

    def get_documentos_usuario(self,user_id):
        data = self.execute_query("select F.* from documento as F, permissao as P, usuario as U where P.perfil_id = U.perfil_id AND P.documento_id = F.documento_id AND U.usuario_id = '{}'".format(user_id))
        return data

    def get_documentos_ids(self):
        data = self.execute_query('''select documento_id from documento''')
        return data

    def edita_documento(self, documento):
        self.execute_query("update documento set documento_tipo = '{}', documento_desc = '{}' where documento_id = '{}'".format(documento.documento_tipo, documento.documento_desc, documento.get_id()), True)

    def get_usuario(self):
        data = self.execute_query("select usuario_id from usuario")
        return data

    def desativa_documento(self, documento_id):
        self.execute_query("update documento set documento_status = 1 where documento_id = \"{}\"".format(documento_id['documento_id']), True)
