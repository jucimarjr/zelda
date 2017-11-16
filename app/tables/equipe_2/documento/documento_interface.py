from flask_mysqldb import MySQL

class DocumentoInterfaceDois:

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
        data = self.execute_query("select * from documento_dois where documento_id = {} limit 1".format(documento_id))

        if len(data) < 1:
            return None

        return data[0]


    def get_documentos_ids_dois(self):
        data = self.execute_query("select * from documento_dois")
        return data

    def desativa_documento(self, documento_id):
        self.execute_query("update documento_dois set documento_status = 1  where documento_id = '{}'".format(documento_id), True)
