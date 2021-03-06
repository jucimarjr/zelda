from ....cursor import db

class DocumentoDois:

    def __init__(self, documento_id = None):
        self.__id = None
        self.__processo_id = None
        self.__descricao = None
        self.__tipo = None
        self.__status = 1

        if documento_id is not None:
            data = db.get_documento_dois(documento_id)

            if data is not None:

                self.__id = documento_id
                self.__id_processo = data['processo_id']
                self.__descricao = data['documento_descricao']
                self.__tipo = data['documento_tipo']
                self.__status = data['documento_status']

    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__descricao

    def get_tipo(self):
        return self.__tipo

    def get_id_processo(self):
        return self.__id_processo

    def get_status(self):
        return self.__status

    def serializa(self):
        return {
                "id": self.get_id(),
                "id_usuario": self.get_id_usuario(),
                "descricao": self.get_descricao(),
                "tipo": self.get_tipo()
                }
    def desativa(self):
        if self.__status != -1:
            self.__status= 1
            db.desativa_documento_dois(self.__id)

    def salva_dois(self, d, t, i):
        if self.get_id() is not None:
            db.edita_documento_dois(d, t, i)
        else:
            self.__id = db.cadastra_documento_dois(d, t, i) 