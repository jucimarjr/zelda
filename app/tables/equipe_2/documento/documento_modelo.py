from ...cursor import db

class Documento:

    def __init__(self, documento_id = None):
        self.__id = None
        self.__id_processo = None
        self.__descricao = None
        self.__tipo = None
        
        if documento_id is not None:
            data = db.get_documento(documento_id)

            if data is not None:

                self.__id = documento_id
                self.__id_processo = data['id_processo']
                self.__descricao = data['descricao']
                self.__tipo = data['tipo']

    def get_id(self):
        return self.__funcionario_id

    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def get_tipo(self):
        return self.__descricao

    def get_id_processo(self):
        return self.__id_processo

    def serializa(self):
        return {
                "id": self.get_id(),
                "id_usuario": self.get_id_usuario(),
                "descricao": self.get_descricao(),
                "tipo": self.get_tipo()
                }

       