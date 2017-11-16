from flask_mysqldb import MySQL

class DocumentoInterface7:

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

    def cadastra_documento(self, documento):
        processo = 2
        if documento.get_processo() is not None:
            if documento.get_processo().get_id() is not None:
                processo = documento.get_processo().get_id()

        self.execute_query("insert into documento (processo_id, descricao, tipo,caminho)\
         values ('{}', '{}', {},'{}')".format(processo, documento.descricao, documento.tipo,documento.caminho), True)
        data = self.execute_query('select LAST_INSERT_ID() as ultimo from documento')
        return data[0]['ultimo']

    def edita_documento(self, documento):
        processo = '2'
        if documento.get_processo() is not None:
            if documento.get_processo().get_id() is not None:
                processo = documento.get_processo().get_id()

        self.execute_query("update documento set processo_id = '{}', descricao = '{}', tipo = {}, caminho = '{}'\
         where documento_id = '{}'".format(processo, documento.descricao, documento.tipo, documento.caminho, documento.get_id()), True)

    def deleta_documento(self, documento_id):
        self.execute_query("delete from documento where documento_id = '{}'".format(documento_id), True)

    def get_documento(self, documento_id):
        data = self.execute_query("select * from documento where documento_id = '{}'".format(documento_id))
        return data

    def get_documento_ids(self):
        data = self.execute_query("select documento_id from documento")
        return data
