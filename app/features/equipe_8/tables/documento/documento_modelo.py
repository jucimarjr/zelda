from ...cursor import db
from  ..processo.processo_modelo import Processo
from app import app

class Documento:
    
    def __init__(self, documento_id=None):

        self.__id = None
        self.descricao = None
        self.tipo = None
        self.caminho = None
        self.__processo_id = None

        if documento_id is not None:
            data = db.get_documento(documento_id)
            if len(data) > 0:
                    self.__id = documento_id
                    self.descricao = data[0][descricao]
                    self.tipo = data[0][tipo]
                    self.caminho = data[0][caminho]
                    self.__processo_id = data[0][processo_id]

    def get_id(self):
        return self.__id

    def get_processo_id(self):
        return self.__processo_id

    def deleta(self):
        db.deleta_documento(self.get_id())

    def salva(self):
        if self.get_id() is None:
            self.__id = db.cadastra_documento(self)
        else:
            db.edita_documento(self)