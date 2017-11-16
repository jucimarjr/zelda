from flask_mysqldb import MySQL

class DocumentoInterfaceOito:

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
        if documento.get_processo() is not None:
            if documento.get_processo().get_id() is not None:
                processo = documento.get_processo().get_id()

        self.execute_query("insert into documento (descricao, tipo, caminho,processo_id)\
         values ('{}', '{}', '{}')".format(documento.descricao, documento.tipo, documento.caminho, documento.get_processo_id()), True)
        data = self.execute_query('select LAST_INSERT_ID() as last from documento')
        return data[0]['last']

    def edita_documento(self, documento):
        perfil = '2'
        if documento.get_processo() is not None:
            if documento.get_processo().get_id() is not None:
                perfil = documento.get_processo().get_id()

        self.execute_query("update documento set descricao = '{}', tipo = '{}', caminho = '{}', processo_id = {}\
         where documento_id = '{}'".format(documento.descricao, documento.tipo, documento.caminho, documento.get_processo_id(), documento.get_id()), True)

    def deleta_documento(self, documento_id):
        self.execute_query("delete from documento where documento_id = '{}'".format(documento_id), True)

    def get_documento(self, documento_id)
        data = self.execute_query("select * from documento where documento_id = '{}'",format(documento_id), True)
        return data