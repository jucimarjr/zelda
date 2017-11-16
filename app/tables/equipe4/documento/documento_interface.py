from flask_mysqldb import MySQL

class DocumentoInterfaceQuatro:

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

    def cadastra_documento(self, documento, processo_id):
        self.execute_query("insert into documento (documento_descricao, documento_tipo, documento_link, processo_id) values ('{}', '{}', '{}', '{}')".format(documento.descricao, documento.tipo, documento.link, processo_id), True)
        data = db.execute_query("select LAST_INSERT_ID() as last FROM documento")
        return data[0]['last']

    def edita_documento(self, documento):
        self.execute_query("update documento set documento_descricao = '{}', documento_tipo = '{}', documento_link = '{}' where documento_id = '{}'".format(documento.descricao, documento.tipo, documento.link, documento.get_id()), True)

    def get_documento(self, documento_id):
        data = self.execute_query("select * from documento where documento_id = '{}' limit 1".format(documento_id))
        return data

    def get_documentos_ids_por_processo(self, processo_id):
        data = self.execute_query("select documento_id from documento where processo_id = '{}'".format(processo_id))
        return data

    def deleta_documento(self, documento_id):
        self.execute_query("delete from documento where documento_id = '{}'".format(documento_id), True)
