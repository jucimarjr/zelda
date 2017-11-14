from .....cursor import db

class DocumentoInterface:
    @staticmethod
    def cadastra_documento(documento, processo_id):
        db.execute_query("INSERT INTO documento (descricao, tipo, processo_id) VALUES ('{}', '{}', '{}')".format(documento.descricao, documento.tipo, processo_id), True)
        data = db.execute_query("SELECT LAST_INSERT_ID() as last FROM documento")
        return data[0]['last']

    @staticmethod
    def edita_documento(documento):
        db.execute_query("UPDATE documento SET descricao = '{}', tipo = '{}' WHERE documento_id = '{}'".format(documento.descricao, documento.tipo, documento.get_id()), True)

    @staticmethod
    def get_documento(id_documento):
        return db.execute_query("SELECT * FROM documento WHERE documento_id = '{}' LIMIT 1".format(id_documento))

    @staticmethod
    def get_documentos_ids_por_processo(id_processo):
        return db.execute_query("SELECT documento_id FROM documento WHERE processo_id = '{}' LIMIT 1".format(id_processo))

    @staticmethod
    def deleta_documento(id_documento):
        db.execute_query("DELETE FROM documento WHERE documento_id = '{}'".format(id_documento), True)